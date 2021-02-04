from math import copysign
from typing import List, Optional

from move.goto import Goto
from move.move import Move
from move.drive import Drive
from move.recovery import Recovery
from utils.vectors import dist
from move.pickup_boost import PickupBoost
from strategy.strategy import Strategy
from rlutilities.simulation import Ball, BoostPad, GameState, BoostPadState
from move.strike.drive_strike import DriveStrike
from rlutilities.linear_algebra import xy, norm, vec2, vec3
from move.strike.double_jump_strike import DoubleJumpStrike


class SoccarStrategy(Strategy):
    def find_base_move(self) -> Move:
        if not self.info.car.on_ground:
            return Recovery(self.info)

        # TODO Kickoff.
        if self.info.state == GameState.Kickoff:
            drive_kickoff: Drive = Drive(
                self.info, vec3(0, 0, self.info.car.hitbox_widths.z)
            )
            drive_kickoff.finished_dist = (
                self.info.ball.collision_radius
                + self.info.car.hitbox_widths.x
                + self.info.car.hitbox_offset.x
            )
            return drive_kickoff

        target: Ball = next(
            (
                ball
                for ball in self.info.ball_prediction
                if DriveStrike.valid_target(self.info.car, ball.position, ball.time)
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
        if double_jump_target.time < target.time - 0.5:
            goal: vec2 = xy(self.info.goals[not self.info.car.team].position)
            return DoubleJumpStrike(self.info, double_jump_target, goal)

        if target.time - self.info.time > 0.6:
            pads: List[BoostPad] = [
                pad
                for pad in self.info.large_pads
                if pad.state == BoostPadState.Available
            ]
            our_goal_position: vec2 = self.info.goals[self.info.car.team].position
            if abs(target.position.x) > 3000:
                if self.info.car.boost < 35 and pads:
                    defensive_position: vec3 = (
                        self.info.car.position + our_goal_position
                    ) / 2
                    pad: BoostPad = min(
                        pads, key=lambda pad: dist(pad.position, defensive_position),
                    )
                    return PickupBoost(self.info, pad)
                elif (
                    (target.position.y - self.info.car.position.y) > 0
                ) == self.info.car.team:
                    backpost: vec3 = vec3(our_goal_position)
                    backpost += 0.125 * (self.info.car.position - backpost)
                    backpost.x = copysign(750, -target.position.x)
                    backpost.z = self.info.car.hitbox_widths.z
                    go_backpost: Goto = Goto(self.info, backpost)
                    go_backpost.drive.finished_dist = 800
                    return go_backpost

        goal: vec2 = xy(self.info.goals[not self.info.car.team].position)
        return DriveStrike(self.info, target, goal)

    def find_interrupt_move(self) -> Optional[Move]:
        if not self.info.car.on_ground and not isinstance(self.move, Recovery):
            return Recovery(self.info)
        return None
