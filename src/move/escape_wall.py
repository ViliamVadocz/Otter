from typing import Optional

from move.move import Move
from move.drive import Drive
from utils.game_info import GameInfo
from rlutilities.mechanics import Jump, Dodge
from rlutilities.simulation import Car
from rlutilities.linear_algebra import xy, dot, sgn, norm, vec2, vec3

MAX_BOOST_ANGLE = 0.3
HANDBRAKE_ANGLE = 1.5
DEFAULT_FINISHED_DIST: float = 140


class EscapeWall(Move):
    def __init__(self, info: GameInfo):
        super().__init__(info)
        self.move: Optional[Move] = None
        self.drive: Drive = Drive(info, self.get_target())

    def update(self):
        if self.move:
            self.interruptible = False
            self.move.step(self.info.dt)
            self.controls = self.move.controls
            self.finished = self.move.finished
            return

        car: Car = self.info.car
        self.drive.target = self.get_target()

        if car.velocity.z > 800:
            # Dodge away from wall.
            direction: vec2 = vec2(car.left() * sgn(dot(car.left(), car.velocity)))
            self.move = Dodge(car)
            self.move.direction = direction
        elif norm(car.velocity) < 1000 and car.forward().z > 0.6:
            # Jump down from wall.
            self.move = Jump(car)

        if self.move:
            self.interruptible = False
            self.move.step(self.info.dt)
            self.controls = self.move.controls
            return

        self.drive.update()
        self.controls = self.drive.controls
        self.finished = not EscapeWall.on_wall(car)

    def get_target(self) -> vec3:
        car: Car = self.info.car
        return xy(car.position + car.up() * 200)

    @staticmethod
    def on_wall(car: Car):
        return car.on_ground and car.up().z < 0.7
