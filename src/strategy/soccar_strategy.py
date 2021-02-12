from math import copysign
from typing import List, Optional

from move.goto import Goto
from move.move import Move
from move.drive import Drive
from utils.const import MAX_CAR_SPEED
from move.recovery import Recovery
from utils.vectors import dist
from move.pickup_boost import PickupBoost
from strategy.strategy import Strategy
from rlutilities.simulation import Ball, BoostPad, GameState, BoostPadState
from move.kickoff.do_kickoff import DoKickoff
from move.strike.jump_strike import JumpStrike
from move.strike.aerial_strike import AerialStrike
from rlutilities.linear_algebra import xy, dot, norm, vec3
from move.strike.double_jump_strike import DoubleJumpStrike

MIN_SAFE_BALL_X = 3000
LOW_BOOST_AMOUNT = 35
BACKPOST_OFFSET_X = 210
BACKPOST_GOAL_CAR_LERP_Y = 0.125
DOUBLE_JUMP_TIME_HANDICAP = 0.5
STRIKE_PRIORITY_TIME = 0.6
AERIAL_TIME_HANDICAP = 0.2


class SoccarStrategy(Strategy):
    def find_base_move(self) -> Move:
        opponent_goal: vec3 = self.info.goals[not self.info.car.team].position
        # TODO Kickoff.
        if self.info.state == GameState.Inactive:
            return DoKickoff(self.info)

        target: Ball = next(
            (
                ball
                for ball in self.info.ball_prediction
                if JumpStrike.valid_target(self.info.car, ball.position, ball.time)
            ),
            self.info.ball_prediction[-1],
        )

        double_jump_target: Ball = next(
            (
                ball
                for ball in self.info.ball_prediction
                if DoubleJumpStrike.valid_target(
                    self.info.car, ball.position, ball.time
                )
            ),
            self.info.ball_prediction[-1],
        )

        aerial_target: Ball = next(
            (
                ball
                for ball in self.info.ball_prediction
                if AerialStrike.valid_target(self.info.car, ball.position, ball.time)
            ),
            self.info.ball_prediction[-1],
        )

        if aerial_target.time < double_jump_target.time - AERIAL_TIME_HANDICAP:
            return AerialStrike(self.info, aerial_target, opponent_goal)
        if not self.info.car.on_ground:
            return Recovery(self.info)
        if double_jump_target.time < target.time - DOUBLE_JUMP_TIME_HANDICAP:
            return DoubleJumpStrike(self.info, double_jump_target, opponent_goal)

        if target.time - self.info.time > STRIKE_PRIORITY_TIME:
            pads: List[BoostPad] = [
                pad
                for pad in self.info.large_pads
                if pad.state == BoostPadState.Available
            ]
            our_goal: vec3 = self.info.goals[self.info.car.team].position
            goal_width: float = self.info.goals[self.info.car.team].width
            if abs(target.position.x) > MIN_SAFE_BALL_X:
                if self.info.car.boost < LOW_BOOST_AMOUNT and pads:
                    defensive_position: vec3 = (self.info.car.position + our_goal) / 2
                    pad: BoostPad = min(
                        pads, key=lambda pad: dist(pad.position, defensive_position),
                    )
                    return PickupBoost(self.info, pad)
                elif dot(our_goal, self.info.car.position - target.position) < 0:
                    backpost: vec3 = vec3(our_goal)
                    backpost += BACKPOST_GOAL_CAR_LERP_Y * (
                        self.info.car.position - backpost
                    )
                    backpost.x = copysign(
                        goal_width / 2 - BACKPOST_OFFSET_X, -target.position.x
                    )
                    backpost.z = self.info.car.hitbox_widths.z
                    go_backpost: Goto = Goto(self.info, backpost)
                    go_backpost.drive.finished_dist = 800
                    return go_backpost

        return JumpStrike(self.info, target, opponent_goal)

    def find_interrupt_move(self) -> Optional[Move]:
        if not self.info.car.on_ground and not isinstance(self.move, Recovery):
            return Recovery(self.info)
        return None
