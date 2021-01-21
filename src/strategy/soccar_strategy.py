from typing import Optional

from move.move import Move
from move.recovery import Recovery
from move.chase_ball import ChaseBall
from move.speed_flip import SpeedFlip
from strategy.strategy import Strategy


class SoccarStrategy(Strategy):
    def find_base_move(self) -> Move:
        return SpeedFlip(self.info)

    def find_replace_move(self) -> Optional[Move]:
        # if not self.info.my_car.on_ground:
        #     return Recovery(self.info)
        return None
