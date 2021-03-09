from math import copysign
from typing import List, Tuple, Mapping, Optional

from tmcp import ActionType, TMCPMessage

from move.goto import Goto
from move.idle import Idle
from move.move import Move
from move.followup import Followup
from move.recovery import Recovery
from utils.vectors import dist, between, alignment, direction
from utils.game_info import GameInfo, team_sign
from move.escape_wall import EscapeWall
from move.pickup_boost import PickupBoost
from strategy.strategy import Strategy
from move.strike.strike import Strike
from rlutilities.simulation import (
    Car,
    Ball,
    BoostPad,
    GameState,
    BoostPadType,
    BoostPadState,
)
from move.kickoff.do_kickoff import DoKickoff
from move.strike.jump_strike import JumpStrike
from move.strike.aerial_strike import AerialStrike
from move.strike.ground_strike import GroundStrike
from rlutilities.linear_algebra import xy, dot, sgn, norm, vec3, normalize
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
        self.goalie = None

    def find_base_move(self) -> Move:
        # Idle.
        if self.info.state == GameState.Inactive:
            self.tmcp_handler.send_ready_action(-1)
            return Idle(self.info)

        # Filter the large-pads for non-reserved active ones.
        pads: List[BoostPad] = [
            pad
            for pad_index, pad in enumerate(self.info.pads)
            if pad.type == BoostPadType.Full
            and pad.state == BoostPadState.Available
            and pad_index not in self.reserved_pads.values()
            and (pad.position.y - self.info.ball.position.y)
            * team_sign(self.info.car.team)
            < -2000
        ]
        pad: Optional[BoostPad] = min(
            pads, key=lambda pad: dist(pad.position, self.info.car.position),
        ) if pads else None

        # Kickoff.
        if self.info.state == GameState.Kickoff:
            if DoKickoff.my_kickoff(self.info):
                self.tmcp_handler.send_ball_action()  # TODO Get some Kickoff time estimate
                return DoKickoff(self.info)

            # Pickup a large boost pad.
            if not pad:
                return Idle(self.info)
            self.tmcp_handler.send_boost_action(self.info.pads.index(pad))
            return PickupBoost(self.info, pad)

        # Recover from being in the air.
        if not self.info.car.on_ground:
            return Recovery(self.info)

        # Get the goals' position.
        our_goal: vec3 = self.info.goals[self.info.car.team].position
        their_goal: vec3 = self.info.goals[not self.info.car.team].position

        # Get the main target (jump strike).
        target: Optional[Ball] = JumpStrike.get_target(self.info)

        # Escape the wall.
        if EscapeWall.on_wall(self.info.car):
            # Strike the ball if available.
            if target and target.time - self.info.time < WALL_STRIKE_TIME:
                self.tmcp_handler.send_ball_action(target.time)
                return JumpStrike(self.info, target, their_goal)
            return EscapeWall(self.info)

        # Get the fastest opponent's jump strike target.
        their_target: Optional[Ball] = min(
            [
                JumpStrike.get_target(self.info, car, step=6)
                for car in self.info.get_opponents()
            ],
            key=lambda target: target.time if target else 10 ** 10,
        )

        # Clear the ball to our corner/away.
        if self.should_clear(target, our_goal):
            clear_goal: vec3 = vec3(their_goal)
            if (
                dist(target.position if target else self.info.ball.position, our_goal)
                < 3000
            ):
                our_corner: vec3 = vec3(our_goal)
                our_corner.x = copysign(
                    self.info.arena.width,
                    target.position.x if target else self.info.ball.position.x,
                )
                our_corner.y *= 0.9
            strike: Strike = self.strike_ball(
                target, clear_goal,
            )
            if strike:
                return strike

        # Strike to their net.
        if self.has_best_touch(target, their_target, their_goal):
            strike: Strike = self.strike_ball(target, their_goal)
            if strike:
                return strike

        # Pickup a large boost pad.
        if (
            pad
            and self.info.car.boost < 60
            and dist(self.info.ball.position, our_goal) > 3000
        ):
            self.tmcp_handler.send_boost_action(self.info.pads.index(pad))
            return PickupBoost(self.info, pad)

        return self.play_defence(target, their_target, our_goal)

    def find_interrupt_move(self) -> Optional[Move]:
        if not self.info.car.on_ground:
            if not isinstance(self.move, Recovery):
                return Recovery(self.info)
        elif not isinstance(self.move, Strike):
            target: Optional[Ball] = JumpStrike.get_target(self.info, step=8)
            our_goal: vec3 = self.info.goals[self.info.car.team].position
            if self.should_clear(target, our_goal, factor=0.85):
                their_goal: vec3 = self.info.goals[not self.info.car.team].position
                strike: Strike = self.strike_ball(target, their_goal)
                if strike:
                    return strike
        return None

    def should_clear(self, target: Ball, our_goal: vec3, factor: float = 1) -> bool:
        if target and dist(target.position, our_goal) < 3500 * factor:
            return True
        return dist(self.info.ball.position, our_goal) < 2500 * factor

    def has_best_touch(
        self, target: Ball, their_target: Optional[Ball], their_goal: vec3
    ) -> bool:
        our_targets: List[Tuple[int, Optional[Ball]]] = [
            (car.id, JumpStrike.get_target(self.info, car, step=6))
            for car in self.info.get_teammates()
        ]
        our_targets.append((self.info.index, target))

        beat_them: List[Tuple[int, Ball]] = [
            (index, this_target)
            for index, this_target in our_targets
            if this_target
            and (not their_target or this_target.time < their_target.time - 0.1)
        ]
        if beat_them:
            return (
                self.info.index
                == max(
                    beat_them,
                    key=lambda index_target: dot(
                        direction(
                            self.info.cars[index_target[0]].position,
                            index_target[1].position,
                        ),
                        direction(index_target[1].position, their_goal),
                    ),
                )[0]
            )

        return not any(
            [
                not target or this_target.time < target.time - 0.1
                for index, this_target in our_targets
                if this_target
                and dot(
                    this_target.position - self.info.cars[index].position,
                    their_goal - this_target.position,
                )
                > 0
            ]
        )

    def play_defence(
        self, target: Optional[Ball], their_target: Optional[Ball], our_goal: vec3
    ) -> Move:
        car: Car = self.info.car

        # Rotate backpost.
        if (
            target
            and dot(
                direction(car.position, target.position),
                direction(car.position, our_goal),
            )
            < -0.2
        ):
            goal_width: float = self.info.goals[car.team].width
            backpost: vec3 = vec3(our_goal)
            backpost += BACKPOST_GOAL_CAR_LERP_Y * (car.position - backpost)
            backpost.x = copysign(
                goal_width / 2 - BACKPOST_OFFSET_X,
                -(target.position.x if target else self.info.ball.position.x),
            )
            if car.position.y * sgn(our_goal.y) - abs(our_goal.y) > -250:
                backpost.x *= -0.75
            backpost.z = car.hitbox_widths.z
            go_backpost: Goto = Goto(self.info, xy(backpost))
            go_backpost.drive.finished_dist = 800
            go_backpost.drive.use_boost = False
            self.tmcp_handler.send_ready_action(-1.0)
            return go_backpost

        # Find a defensive position.
        teammates: List[Car] = self.info.get_teammates()
        teammates_behind: List[Car] = [
            mate
            for mate in teammates
            if (mate.position.y - car.position.y) * team_sign(car.team) < 0
        ]
        defensive_position: vec3 = (
            our_goal
            + (their_target.position - our_goal)
            * min(1, 1.25 * len(teammates_behind) / len(teammates))
        ) if their_target else our_goal

        # Pickup small pads.
        if car.boost < 90:
            small_pads: List[BoostPad] = [
                pad
                for pad_index, pad in enumerate(self.info.pads)
                if pad.type == BoostPadType.Partial
                and pad.state == BoostPadState.Available
                and pad_index not in self.reserved_pads.values()
            ]
            if small_pads:
                pad: BoostPad = max(
                    small_pads,
                    key=lambda pad: between(
                        car.position, pad.position, defensive_position
                    ),
                )
                if between(car.position, pad.position, defensive_position) > max(
                    0.3, car.boost / 100
                ):
                    return PickupBoost(self.info, pad)

        go_defense: Goto = Goto(self.info, xy(defensive_position))
        go_defense.drive.finished_dist = 3000
        go_defense.drive.target_speed = dist(car.position, defensive_position)
        go_defense.drive.use_boost = False
        self.tmcp_handler.send_ready_action(target.time if target else -1)
        return go_defense

    def strike_ball(self, target: Optional[Ball], goal: vec3) -> Optional[Strike]:
        car: Car = self.info.car

        # Go for an aerial-strike.
        aerial_target: Optional[Ball] = AerialStrike.get_target(self.info, step=2)
        if aerial_target and (
            not target
            or (
                dot(car.velocity, direction(car.position, aerial_target.position),) > 0
                and dot(car.velocity, direction(car.position, target.position),) < 0
            )
        ):
            self.tmcp_handler.send_ball_action(aerial_target.time)
            return AerialStrike(self.info, aerial_target, goal)

        # Go for a double-jump-strike.
        double_jump_target: Optional[Ball] = DoubleJumpStrike.get_target(self.info)
        if double_jump_target and (
            not target
            or double_jump_target.time < target.time - DOUBLE_JUMP_TIME_HANDICAP
        ):
            self.tmcp_handler.send_ball_action(double_jump_target.time)
            return DoubleJumpStrike(self.info, double_jump_target, goal)

        # Go for a jump-strike.
        if not target:
            return None
        self.tmcp_handler.send_ball_action(target.time)
        return JumpStrike(self.info, target, goal)

    def handle_tmcp_message(self, message: TMCPMessage):
        # Remove pad reservation if we get a new message from that bot.
        if self.reserved_pads.get(message.index):
            self.reserved_pads[message.index] = None

        # Also remove pad reservations if the bot gets close.
        for bot_index, pad_index in self.reserved_pads.items():
            if pad_index is None:
                continue
            if (
                dist(
                    self.info.cars[bot_index].position,
                    self.info.pads[pad_index].position,
                )
                < 200
            ):
                self.reserved_pads[bot_index] = None

        # Reserve a pad.
        if message.action_type == ActionType.BOOST:
            pad_index = message.target
            self.reserved_pads[message.index] = pad_index

            # Another bot is trying to reserve a pad we are already going for.
            if (
                isinstance(self.move, PickupBoost)
                and self.move.pad == self.info.pads[pad_index]
            ):
                pad_pos = self.info.pads[pad_index].position
                # Repeat the message if we are closer.
                if dist(self.info.car.position, pad_pos) < dist(
                    self.info.cars[message.index].position, pad_pos
                ):
                    self.tmcp_handler.send_boost_action(pad_index)

                # Go do something else if they're closer.
                else:
                    self.move.finished = True

        # Keep track of goalie.
        if self.goalie is not None and message.index == self.goalie:
            self.goalie = None
        if message.action_type == ActionType.DEFEND:
            self.goalie = message.index
