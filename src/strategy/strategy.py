from abc import ABC, abstractmethod
from typing import Optional

from utils import rendering
from move.move import Move
from utils.const import MAX_CAR_SPEED
from utils.vectors import dist
from utils.game_info import GameInfo
from rlutilities.simulation import Input, GameState
from rlutilities.linear_algebra import vec3


class Strategy(ABC):
    def __init__(self, info: GameInfo):
        self.info: GameInfo = info
        self.move: Optional[Move] = None
        self.controls: Input = Input()
        self.last_demolished: bool = False
        self.last_inactive: bool = False
        self.last_position: vec3 = vec3(0, 0, 0)

    @abstractmethod
    def find_base_move(self) -> Move:
        pass

    def find_interrupt_move(self) -> Optional[Move]:
        return None

    def update(self):
        # Force end move...
        # ... if no longer demolished.
        if not self.info.car.demolished and self.last_demolished:
            self.move = None
        self.last_demolished = self.info.car.demolished
        # ... if newly inactive.
        if (self.info.state == GameState.Inactive) and not self.last_inactive:
            self.move = None
        self.last_inactive = self.info.state == GameState.Inactive
        # ... if teleported.
        if (
            dist(self.info.car.position, self.last_position)
            > (MAX_CAR_SPEED + 200) * self.info.dt
        ):
            self.move = None
        self.last_position = vec3(self.info.car.position)

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
