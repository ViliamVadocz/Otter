from abc import ABC, abstractmethod
from typing import Optional

from move.move import Move
from utils.game_info import GameInfo
from rlutilities.simulation import Input


class Strategy(ABC):
    def __init__(self, info: GameInfo):
        self.info: GameInfo = info
        self.move: Optional[Move] = None
        self.controls = Input()

    def find_replace_move(self) -> Optional[Move]:
        return None

    @abstractmethod
    def find_base_move(self) -> Move:
        pass

    def update(self):
        for _ in range(5):
            if self.move and not self.move.finished:
                replace_move: Optional[Move] = self.find_replace_move()
                if replace_move:
                    self.move = replace_move
            else:
                self.move = self.find_base_move()
            self.move.update()
            if not self.move.finished:
                break
        if self.move:
            self.controls = self.move.controls
