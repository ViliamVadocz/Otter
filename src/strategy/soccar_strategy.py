from math import copysign
from typing import List, Optional

from move.goto import Goto
from move.move import Move
from move.drive import Drive
from utils.const import BOOST_ACC, MAX_CAR_SPEED, MAX_JUMP_HEIGHT, MAX_NO_BOOST_SPEED
from move.recovery import Recovery
from strategy.strategy import Strategy
from rlutilities.simulation import Ball, BoostPad, BoostPadType, BoostPadState
from move.strike.drive_strike import DriveStrike
from rlutilities.linear_algebra import xy, dot, norm, vec2, vec3, normalize


class SoccarStrategy(Strategy):
    def find_base_move(self) -> Move:
        if not self.info.car.on_ground:
            return Recovery(self.info)

        target: Ball = None
        if norm(xy(self.info.ball.position)) < 1:
            target = self.info.ball
        else:

            def can_intercept(ball: Ball) -> bool:
                height: float = dot(
                    ball.position - self.info.car.position, self.info.car.up()
                )
                if not (0 < height < MAX_JUMP_HEIGHT + 60):
                    return False
                t: float = max(1e-10, ball.time - self.info.time)
                u: float = dot(
                    self.info.car.velocity,
                    normalize(ball.position - self.info.car.position),
                )
                s: float = norm(ball.position - self.info.car.position) - abs(height)
                return (2 * s) / t - u < 0.95 * max(
                    MAX_NO_BOOST_SPEED,
                    min(MAX_CAR_SPEED, abs(u) + self.info.car.boost / 33 * BOOST_ACC),
                )

            target: Ball = next(
                (ball for ball in self.info.ball_prediction if can_intercept(ball)),
                self.info.ball_prediction[-1],
            )

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
                            pads,
                            key=lambda pad: norm(pad.position - defensive_position),
                        )
                        return Goto(self.info, pad.position)
                    elif (
                        (target.position.y - self.info.car.position.y) < 0
                    ) == self.info.car.team:
                        backpost: vec3 = vec3(our_goal_position)
                        backpost += 0.125 * (self.info.car.position - backpost)
                        backpost.x = copysign(750, -target.position.x)
                        backpost.z = self.info.car.hitbox_widths.z
                        return Goto(self.info, backpost)
        goal: vec2 = xy(self.info.goals[not self.info.car.team].position)
        return DriveStrike(self.info, target, goal)

    def find_interrupt_move(self) -> Optional[Move]:
        if not self.info.car.on_ground and not isinstance(self.move, Recovery):
            return Recovery(self.info)
        return None
