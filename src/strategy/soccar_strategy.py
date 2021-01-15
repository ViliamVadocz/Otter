from typing import Optional

from strategy.strategy import Strategy
from move.chase_ball import ChaseBall
from move.recovery import Recovery
from move.move import Move


class SoccarStrategy(Strategy):
    def find_base_move(self) -> Move:
        return ChaseBall(self.info)

    def find_replace_move(self) -> Optional[Move]:
        if not self.info.my_car.on_ground:
            return Recovery(self.info)
        return None
