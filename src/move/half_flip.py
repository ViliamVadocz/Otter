from move.move import Move
from utils.game_info import GameInfo
from rlutilities.mechanics import ReorientML as Reorient
from rlutilities.simulation import Input
from rlutilities.linear_algebra import xy, look_at, normalize

FIRST_JUMP = 0.05
NO_JUMP = 0.05
DODGE_BACK = 0.2
FLIP_CANCEL = 0.2
ROTATE = 0.5


class HalfFlip(Move):
    def __init__(self, info: GameInfo):
        super().__init__(info)

        self.timer = 0.0
        self.reorient = Reorient(self.info.car)
        self.interruptible = False

    def update(self):
        self.controls = Input()
        if self.timer < FIRST_JUMP:
            self.controls.throttle = -1.0
            self.controls.jump = True
        elif self.timer < FIRST_JUMP + NO_JUMP:
            self.controls.throttle = -1.0
            self.controls.jump = False
            self.controls.pitch = 1.0
        elif self.timer < FIRST_JUMP + NO_JUMP + DODGE_BACK:
            self.controls.jump = True
            self.controls.pitch = 1.0
        elif self.timer < FIRST_JUMP + NO_JUMP + DODGE_BACK + FLIP_CANCEL:
            self.controls.throttle = 1.0
            self.controls.pitch = -1.0
        elif self.timer < FIRST_JUMP + NO_JUMP + DODGE_BACK + FLIP_CANCEL + ROTATE:
            self.controls.throttle = 1.0
            self.controls.pitch = -1.0
            self.controls.yaw = -1.0
            self.controls.roll = 1.0
        else:
            # If still not on ground, we should let Recovery handle this.
            self.finished = True

        self.timer += self.info.dt
        self.finished = self.info.car.on_ground and self.timer > FIRST_JUMP + NO_JUMP
