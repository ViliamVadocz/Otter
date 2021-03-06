from move.move import Move
from utils.const import MAX_CAR_SPEED
from utils.game_info import GameInfo
from rlutilities.linear_algebra import norm

STABILIZE = 0.1
FIRST_JUMP = 0.1
BETWEEN_JUMPS = 0.1
SECOND_JUMP = 0.05
TIMEOUT = 1.5


class SpeedFlip(Move):
    def __init__(self, info: GameInfo, spin_right=True, use_boost=True):
        super().__init__(info)
        self.direction = 1.0 if spin_right else -1.0
        self.use_boost = use_boost
        self.timer = 0.0

    def update(self):
        car = self.info.car

        self.controls.throttle = 1.0
        self.controls.boost = (
            self.use_boost and norm(car.velocity) < MAX_CAR_SPEED - 100
        )

        if self.timer < STABILIZE:
            pass

        elif self.timer < STABILIZE + FIRST_JUMP:
            self.controls.jump = True
            self.controls.pitch = 1.0

        elif self.timer < STABILIZE + FIRST_JUMP + BETWEEN_JUMPS:
            self.controls.jump = False
            self.controls.pitch = 1.0

        elif self.timer < STABILIZE + FIRST_JUMP + BETWEEN_JUMPS + SECOND_JUMP:
            self.controls.jump = True
            self.controls.pitch = -1.0
            self.controls.roll = 0.3 * self.direction

        else:
            self.controls.jump = False
            self.controls.pitch = 1.0
            self.controls.roll = self.direction
            self.controls.yaw = self.direction

        self.timer += self.info.dt
        self.finished = (self.timer > TIMEOUT) or (car.on_ground and self.timer > 0.5)
