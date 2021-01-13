from abc import ABC, abstractmethod

from rlutilities.simulation import Input
from utils.game_info import GameInfo


class Move(ABC):
    def __init__(self, info: GameInfo):
        self.info: GameInfo = info
        self.controls: Input = Input()
        self.finished: bool = False

    @abstractmethod
    def update(self):
        pass
