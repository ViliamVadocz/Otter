from abc import ABC, abstractmethod
from typing import Optional

from rlbot.utils.rendering.rendering_manager import RenderingManager

from move.move import Move
from utils.game_info import GameInfo
from rlutilities.simulation import Input


class Strategy(ABC):
    def __init__(self, info: GameInfo, renderer: RenderingManager):
        self.info: GameInfo = info
        self.renderer: RenderingManager = renderer
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
        self.move.update()
        self.controls = self.move.controls
        self.renderer.begin_rendering("move")
        self.move.render(self.renderer)
        self.renderer.end_rendering()
