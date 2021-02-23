from math import copysign
from typing import List, Mapping, Optional

from move.goto import Goto
from move.idle import Idle
from move.move import Move
from utils.tmcp import ActionType, TMCPMessage
from move.recovery import Recovery
from utils.vectors import dist, alignment
from move.escape_wall import EscapeWall
from move.pickup_boost import PickupBoost
from strategy.strategy import Strategy
from rlutilities.simulation import (
    Ball,
    BoostPad,
    GameState,
    BoostPadType,
    BoostPadState,
)
from move.kickoff.do_kickoff import DoKickoff
from move.strike.jump_strike import JumpStrike
from move.strike.aerial_strike import AerialStrike
from rlutilities.linear_algebra import xy, dot, norm, vec3, normalize
from move.strike.double_jump_strike import DoubleJumpStrike

MIN_SAFE_BALL_X = 3000
LOW_BOOST_AMOUNT = 35
BACKPOST_OFFSET_X = 210
BACKPOST_GOAL_CAR_LERP_Y = 0.125
DOUBLE_JUMP_TIME_HANDICAP = 0.5
STRIKE_PRIORITY_TIME = 0.6
AERIAL_TIME_HANDICAP = 0.2
MIN_AERIAL_ALIGNMENT = 0.3
WALL_STRIKE_TIME: float = 3


class SoccarStrategy(Strategy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reserved_pads: Mapping[int, int] = dict()

    def find_base_move(self) -> Move:
        # Idle.
        if self.info.state == GameState.Inactive:
            return Idle(self.info)

        # Filter the large-pads for non-reserved active ones.
        pads: List[BoostPad] = [
            pad
            for pad_index, pad in enumerate(self.info.pads)
            if pad.type == BoostPadType.Full
            and pad.state == BoostPadState.Available
            and pad_index not in self.reserved_pads.values()
        ]

        # Kickoff.
        if self.info.state == GameState.Kickoff:
            closer: List[bool] = [
                norm(car.position) + car.id
                < norm(self.info.car.position) + self.info.index
                for car in self.info.get_teammates()
            ]
            if any(closer):
                pad: BoostPad = min(
                    pads, key=lambda pad: dist(pad.position, self.info.car.position),
                )
                # Reserve boost pad.
                self.tmcp_handler.send_boost_action(self.info.pads.index(pad))
                return PickupBoost(self.info, pad)
            self.tmcp_handler.send_ball_action()  # TODO Get some Kickoff time estimate
            return DoKickoff(self.info)

        opponent_goal: vec3 = self.info.goals[not self.info.car.team].position

        target: Ball = next(
            (
                ball
                for ball in self.info.ball_prediction
                if JumpStrike.valid_target(
                    self.info, self.info.car, ball.position, ball.time
                )
            ),
            self.info.ball_prediction[-1],
        )

        # Escape the wall.
        if EscapeWall.on_wall(self.info.car):
            # Strike the ball if possible.
            if target.time - self.info.time < WALL_STRIKE_TIME:
                self.tmcp_handler.send_ball_action(target.time)
                return JumpStrike(self.info, target, opponent_goal)
            return EscapeWall(self.info)

        double_jump_target: Ball = next(
            (
                ball
                for ball in self.info.ball_prediction
                if DoubleJumpStrike.valid_target(
                    self.info, self.info.car, ball.position, ball.time
                )
            ),
            self.info.ball_prediction[-1],
        )

        aerial_target: Ball = next(
            (
                ball
                for ball in self.info.ball_prediction
                if alignment(
                    self.info.car.position,
                    ball.position,
                    opponent_goal,
                    normalize(self.info.gravity),
                )
                > MIN_AERIAL_ALIGNMENT
                and AerialStrike.valid_target(
                    self.info, self.info.car, ball.position, ball.time, opponent_goal
                )
            ),
            self.info.ball_prediction[-1],
        )

        # Go for an aerial-strike.
        if aerial_target.time < double_jump_target.time - AERIAL_TIME_HANDICAP or (
            not self.info.car.on_ground and aerial_target.time - self.info.time < 0.5
        ):
            self.tmcp_handler.send_ball_action(aerial_target.time)
            return AerialStrike(self.info, aerial_target, opponent_goal)

        # Recover from being in the air.
        if not self.info.car.on_ground:
            return Recovery(self.info)

        # Define our goal's position.
        our_goal: vec3 = self.info.goals[self.info.car.team].position
        goal_width: float = self.info.goals[self.info.car.team].width

        # Use the positioning of our teammates to determine whether to go for the ball.
        teammate_behind: bool = False
        if not self.info.get_teammates() or dist(target.position, our_goal) < 3000:
            teammate_behind = True
        else:
            for car in self.info.get_teammates():
                car_position: vec3 = car.position + car.velocity * (
                    target.time - car.time
                )
                teammate_behind = (
                    dot(
                        car_position - self.info.car.position,
                        self.info.car.position - target.position,
                    )
                    > 0
                )
                if teammate_behind:
                    break

        # Choose to grab boost or rotate to backpost.
        if target.time - self.info.time > STRIKE_PRIORITY_TIME:
            if abs(target.position.x) > MIN_SAFE_BALL_X:
                # Grab boost.
                if self.info.car.boost < LOW_BOOST_AMOUNT and pads:
                    defensive_position: vec3 = (self.info.car.position + our_goal) / 2
                    pad: BoostPad = min(
                        pads, key=lambda pad: dist(pad.position, defensive_position),
                    )
                    # Reserve boost pad.
                    self.tmcp_handler.send_boost_action(self.info.pads.index(pad))
                    return PickupBoost(self.info, pad)
                elif dot(our_goal, self.info.car.position - target.position) < 0:
                    # Rotate backpost.
                    backpost: vec3 = vec3(our_goal)
                    backpost += BACKPOST_GOAL_CAR_LERP_Y * (
                        self.info.car.position - backpost
                    )
                    backpost.x = copysign(
                        goal_width / 2 - BACKPOST_OFFSET_X, -target.position.x
                    )
                    backpost.z = self.info.car.hitbox_widths.z
                    go_backpost: Goto = Goto(self.info, xy(backpost))
                    go_backpost.drive.finished_dist = 800
                    self.tmcp_handler.send_wait_action()
                    return go_backpost

        # Go defend if a teammate isn't backing up our strike.
        if not teammate_behind:
            defensive_position: vec3 = self.info.ball.position + (
                our_goal - self.info.ball.position
            ) * 0.8
            go_defense: Goto = Goto(self.info, xy(defensive_position))
            go_defense.drive.finished_dist = 2000
            self.tmcp_handler.send_wait_action()
            return go_defense

        # Go for a double-jump-strike.
        if double_jump_target.time < target.time - DOUBLE_JUMP_TIME_HANDICAP:
            self.tmcp_handler.send_ball_action(double_jump_target.time)
            return DoubleJumpStrike(self.info, double_jump_target, opponent_goal)

        # Go for a jump-strike.
        self.tmcp_handler.send_ball_action(target.time)
        return JumpStrike(self.info, target, opponent_goal)

    def find_interrupt_move(self) -> Optional[Move]:
        if not self.info.car.on_ground:
            if not isinstance(self.move, Recovery):
                return Recovery(self.info)
        elif EscapeWall.on_wall(self.info.car):
            if not isinstance(self.move, EscapeWall):
                return EscapeWall(self.info)
        return None

    def handle_tmcp_message(self, message: TMCPMessage):
        # Remove pad reservation if we get a new message from that bot.
        if self.reserved_pads.get(message.index):
            self.reserved_pads[message.index] = None
        # Also remove pad reservations if the bot gets close.
        for bot_index, pad_index in self.reserved_pads.items():
            if pad_index is None:
                continue
            if dist(self.info.cars[bot_index], self.info.pads[pad_index]) < 200:
                self.reserved_pads[bot_index] = None

        # Handle different types of messages.
        if message.action_type == ActionType.BALL:
            pass
        elif message.action_type == ActionType.BOOST:
            pad_index = message.target
            self.reserved_pads[message.index] = pad_index
        elif message.action_type == ActionType.DEMO:
            pass
        elif message.action_type == ActionType.WAIT:
            pass
