from typing import Optional

from tmcp import TMCPMessage

from move.idle import Idle
from move.move import Move
from move.recovery import Recovery
from strategy.strategy import Strategy
from move.nav.nav_strike import NavStrike


class TestStrategy(Strategy):
    def find_base_move(self) -> Move:
        follow = NavStrike.plan_path(self.info)
        if follow:
            return NavStrike(self.info, follow)
        return Idle(self.info)

    def find_interrupt_move(self) -> Optional[Move]:
        if not self.info.car.on_ground:
            if not isinstance(self.move, Recovery):
                return Recovery(self.info)

    def handle_tmcp_message(self, message: TMCPMessage):
        pass
