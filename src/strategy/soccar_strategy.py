from typing import Optional

from move.move import Move
from move.aerial import Aerial
from move.recovery import Recovery
from move.chase_ball import ChaseBall
from move.speed_flip import SpeedFlip
from strategy.strategy import Strategy
from rlutilities.linear_algebra import vec3


class SoccarStrategy(Strategy):
    def find_base_move(self) -> Move:
        return Recovery(self.info)

    def find_interrupt_move(self) -> Optional[Move]:
        if self.info.my_car.on_ground and not isinstance(self.move, Aerial):
            # frame = self.info.ball_prediction.slices[120]
            # target = vec3(
            #     frame.physics.location.x,
            #     frame.physics.location.y,
            #     frame.physics.location.z,
            # )
            # time = frame.game_seconds
            return Aerial(self.info, vec3(0, 0, 800), self.info.time + 3.0)
        return None
