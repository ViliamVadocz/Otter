from move.move import Move
from utils.const import MAX_FIRST_JUMP_HOLD
from utils.vectors import dist
from utils.game_info import GameInfo
from rlutilities.linear_algebra import vec3

FINISHED_DIST = 100
TIMEOUT = 1.5


class DoubleJump(Move):
    def __init__(self, info: GameInfo, target: vec3):
        super().__init__(info)
        self.target = target
        self.timer = 0.0

    def update(self):
        if self.timer < MAX_FIRST_JUMP_HOLD:
            self.controls.jump = True
        elif self.timer < MAX_FIRST_JUMP_HOLD + 2 * self.info.dt:
            self.controls.jump = False
        elif self.timer < MAX_FIRST_JUMP_HOLD + 4 * self.info.dt:
            self.controls.jump = True
            self.controls.pitch = 0.0
            self.controls.yaw = 0.0
            self.controls.roll = 0.0
            self.controls.steer = 0.0
        else:
            self.finished = True

        self.timer += self.info.dt
        self.finished = (
            dist(self.info.car.position, self.target) < FINISHED_DIST
            or self.info.car.on_ground
            and self.timer > MAX_FIRST_JUMP_HOLD
            or self.timer > TIMEOUT
        )
