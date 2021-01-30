from move.move import Move
from utils.game_info import GameInfo
from rlutilities.mechanics import ReorientML as Reorient
from rlutilities.simulation import Input
from rlutilities.linear_algebra import xy, look_at, normalize

FIRST_JUMP = 0.05
NO_JUMP = 0.05
DODGE_BACK = 0.2
FLIP_CANCEL = 0.2
ROTATE = 0.4
TIMEOUT = 1.5


class HalfFlip(Move):
    def __init__(self, info: GameInfo):
        super().__init__(info)

        self.timer = 0.0
        self.reorient = Reorient(self.info.car)

    def update(self):
        self.controls = Input()
        if self.timer < FIRST_JUMP:
            self.controlsthrottle = -1.0
            self.controls.jump = True
        elif self.timer < FIRST_JUMP + NO_JUMP:
            self.controls.jump = False
            self.controls.pitch = 1.0
        elif self.timer < FIRST_JUMP + NO_JUMP + DODGE_BACK:
            self.controls.jump = True
            self.controls.pitch = 1.0
        elif self.timer < FIRST_JUMP + NO_JUMP + DODGE_BACK + FLIP_CANCEL:
            self.controls.pitch = -1.0
        elif self.timer < FIRST_JUMP + NO_JUMP + DODGE_BACK + FLIP_CANCEL + ROTATE:
            self.controls.pitch = -1.0
            self.controls.yaw = -1.0
            self.controls.roll = 1.0
        else:
            # If we are still not done, use RLU Reorient to align with velocity.
            self.reorient.target_orientation = look_at(
                normalize(xy(self.info.car.velocity)), normalize(-1 * self.info.gravity)
            )
            self.reorient.step(self.info.dt)
            self.controls = self.reorient.controls
            self.controls.throttle = 1.0

        self.timer += self.info.dt
        self.finished = (self.timer > TIMEOUT) or (
            self.info.car.on_ground and self.timer > FIRST_JUMP + NO_JUMP
        )
