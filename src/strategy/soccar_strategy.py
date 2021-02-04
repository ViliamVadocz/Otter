from math import copysign
from typing import List, Optional

from utils import rendering
from move.goto import Goto
from move.move import Move
from move.drive import Drive
from move.recovery import Recovery
from utils.vectors import dist
from move.pickup_boost import PickupBoost
from strategy.strategy import Strategy
from rlutilities.simulation import Ball, BoostPad, GameState, BoostPadState
from move.strike.drive_strike import DriveStrike
from rlutilities.linear_algebra import xy, dot, norm, vec3
from move.strike.double_jump_strike import DoubleJumpStrike

MAX_STRIKE_TIME = 1.5
MAX_BALL_X_DIST = 3000
LOW_BOOST_AMOUNT = 35
BACKPOST_OFFSET_X = 150
BACKPOST_GOAL_CAR_LERP_Y = 0.125


class SoccarStrategy(Strategy):
    def find_base_move(self) -> Move:
        if not self.info.car.on_ground:
            return Recovery(self.info)

        # TODO Kickoff.
        if (
            self.info.state == GameState.Kickoff
            or norm(xy(self.info.ball.position)) < 1
        ):
            drive_kickoff: Drive = Drive(
                self.info, vec3(0, 0, self.info.car.hitbox_widths.z)
            )
            drive_kickoff.finished_dist = (
                self.info.ball.collision_radius
                + self.info.car.hitbox_widths.x
                + self.info.car.hitbox_offset.x
            )
            return drive_kickoff

        opponent_goal: vec3 = self.info.goals[not self.info.car.team].position
        for ball in self.info.ball_prediction:
            if (
                ball.time - self.info.time > MAX_STRIKE_TIME
                and abs(ball.position.x) > MAX_BALL_X_DIST
            ):
                break
            if DriveStrike.valid_target(self.info.car, ball.position, ball.time):
                return DriveStrike(self.info, ball, xy(opponent_goal))
            if DoubleJumpStrike.valid_target(self.info.car, ball.position, ball.time):
                return DoubleJumpStrike(self.info, ball, xy(opponent_goal))
        # `ball` is still defined as the last one we iterated over

        pads: List[BoostPad] = [
            pad for pad in self.info.large_pads if pad.state == BoostPadState.Available
        ]
        our_goal: vec3 = self.info.goals[self.info.car.team].position
        goal_width = self.info.goals[self.info.car.team].width
        if self.info.car.boost < LOW_BOOST_AMOUNT and pads:
            defensive_position: vec3 = (self.info.car.position + our_goal) / 2
            pad: BoostPad = min(
                pads, key=lambda pad: dist(pad.position, defensive_position)
            )
            return PickupBoost(self.info, pad)
        elif dot(our_goal, self.info.car.position - ball.position) < 0:
            backpost = our_goal + BACKPOST_GOAL_CAR_LERP_Y * (
                self.info.car.position - our_goal
            )
            backpost.x = copysign(goal_width - BACKPOST_OFFSET_X, -ball.position.x)
            backpost.z = self.info.car.hitbox_widths.z
            go_backpost: Goto = Goto(self.info, backpost)
            go_backpost.drive.finished_dist = 800
            return go_backpost
        else:
            go_offensive = Goto(self.info, ball.position)
            go_offensive.drive.finished_dist = 1500
            return go_offensive

    def find_interrupt_move(self) -> Optional[Move]:
        if not self.info.car.on_ground and not isinstance(self.move, Recovery):
            return Recovery(self.info)
        return None
