from math import inf

from move.move import Move
from utils.const import MAX_FIRST_JUMP_HOLD
from utils.game_info import GameInfo
from rlutilities.mechanics import Aerial as RLUAerial
from rlutilities.simulation import Input
from rlutilities.linear_algebra import vec3

FIRST_JUMP = MAX_FIRST_JUMP_HOLD
BETWEEN_JUMPS = 0.02
SECOND_JUMP = 0.02


class Aerial(Move):
    def __init__(self, info: GameInfo, target: vec3, arrival_time: float, up: vec3):
        super().__init__(info)

        self.aerial = RLUAerial(info.car)
        self.aerial.target_position = target
        self.aerial.arrival_time = arrival_time
        self.aerial.up = up

        self.timer: float = inf

    def update(self):

        # Fast aerial double jump.
        if self.info.car.on_ground and self.timer > FIRST_JUMP:
            self.controls = Input()
            self.timer = 0.0
        if self.timer < FIRST_JUMP:
            self.controls.jump = True
            self.controls.boost = True
            self.controls.pitch = 1.0
        elif self.timer < FIRST_JUMP + BETWEEN_JUMPS:
            self.controls.jump = False
            self.controls.boost = True
            self.controls.pitch = 1.0
        elif self.timer < FIRST_JUMP + BETWEEN_JUMPS + SECOND_JUMP:
            self.controls.jump = True
            self.controls.boost = True
            self.controls.pitch = 0.0
        # RLU mechanic once in the air.
        else:
            self.aerial.step(self.info.dt)
            self.controls = self.aerial.controls

        self.timer += self.info.dt
        self.finished = (
            self.info.time > self.aerial.arrival_time or self.aerial.finished
        )
