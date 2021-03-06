from typing import Optional

from tmcp import TMCPMessage

from move.idle import Idle
from move.move import Move
from strategy.strategy import Strategy


class DefaultStrategy(Strategy):
    def find_base_move(self) -> Move:
        return Idle(self.info)

    def find_interrupt_move(self) -> Optional[Move]:
        return None

    def update(self):
        pass

    def handle_tmcp_message(self, message: TMCPMessage):
        pass
