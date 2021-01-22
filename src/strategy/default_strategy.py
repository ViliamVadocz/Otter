from typing import Optional

from move.move import Move
from strategy.strategy import Strategy


class DefaultStrategy(Strategy):
    def find_base_move(self) -> Move:
        return None

    def find_replace_move(self) -> Optional[Move]:
        return None

    def update(self):
        pass
