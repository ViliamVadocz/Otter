from abc import ABC, abstractmethod
from typing import Optional

from utils import rendering
from move.move import Move
from utils.game_info import GameInfo
from rlutilities.simulation import Input


class Strategy(ABC):
    def __init__(self, info: GameInfo):
        self.info: GameInfo = info
        self.move: Optional[Move] = None
        self.controls: Input = Input()

    @abstractmethod
    def find_base_move(self) -> Move:
        pass

    def find_interrupt_move(self) -> Optional[Move]:
        return None

    def update(self):
        # Choose move.
        if self.move and not self.move.finished:
            if self.move.interruptible:
                interrupt_move: Optional[Move] = self.find_interrupt_move()
                if interrupt_move:
                    self.move = interrupt_move
        else:
            self.move = self.find_base_move()

        # Update.
        rendering.begin_rendering("move")
        rendering.draw_string_3d(
            self.info.car.position,
            1,
            1,
            str(self.move.__class__.__name__),
            rendering.white(),
        )
        self.move.update()
        rendering.end_rendering()
        self.controls = self.move.controls
