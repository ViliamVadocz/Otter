from math import inf

from move.move import Move
from utils.game_info import GameInfo
from rlutilities.mechanics import Aerial as RLUAerial
from rlutilities.linear_algebra import mat3, vec3


class Aerial(Move):
    def __init__(
        self, info: GameInfo, target: vec3, arrival_time: float, orientation: mat3
    ):
        super().__init__(info)

        self.aerial = RLUAerial(info.car)
        self.aerial.target_position = target
        self.aerial.arrival_time = arrival_time
        self.aerial.target_orientation = orientation
        self.aerial.double_jump = True

        self.timer: float = inf

    def update(self):
        # Just use the RLU Mechanic
        self.aerial.step(self.info.dt)
        self.controls = self.aerial.controls

        self.timer += self.info.dt
        self.finished = (
            self.info.time > self.aerial.arrival_time or self.aerial.finished
        )
