from typing import Optional

from move.move import Move
from move.recovery import Recovery
from strategy.strategy import Strategy
from rlutilities.simulation import Ball
from move.strike.drive_strike import DriveStrike
from rlutilities.linear_algebra import xy, norm, vec2


class SoccarStrategy(Strategy):
    def find_base_move(self) -> Move:
        target: Ball = min(
            self.info.ball_prediction,
            key=lambda ball: abs(
                norm(self.info.car.position - ball.position)
                / max(1e-10, ball.time - self.info.time)
                - 1410
            ),
        )
        goal: vec2 = xy(self.info.goals[not self.info.car.team].position)
        return DriveStrike(self.info, target, goal)

    def find_interrupt_move(self) -> Optional[Move]:
        if not self.info.car.on_ground and not isinstance(self.move, Recovery):
            return Recovery(self.info)
        return None
