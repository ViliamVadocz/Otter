from strategy.strategy import Strategy
from move.chase_ball import ChaseBall
from move.move import Move


class SoccarStrategy(Strategy):
    def find_base_move(self) -> Move:
        return ChaseBall(self.info)
