from abc import ABC, abstractmethod

from utils.game_info import GameInfo
from rlutilities.simulation import Input


class Move(ABC):
    def __init__(self, info: GameInfo):
        self.info: GameInfo = info
        self.controls: Input = Input()
        self.finished: bool = False
        self.interruptible: bool = True

    @abstractmethod
    def update(self):
        pass
