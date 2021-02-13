from math import sin

from move.move import Move
from utils.game_info import GameInfo
from rlutilities.simulation import GameState


class Idle(Move):
    def __init__(self, info: GameInfo):
        super().__init__(info)
        self.interruptible: bool = False

    def update(self):
        # Wait until kickoff.
        self.finished = self.info.state != GameState.Inactive
        self.controls.steer = sin(self.info.time * 14)  # Wiggle.
        self.controls.throttle = self.info.car.on_ground
