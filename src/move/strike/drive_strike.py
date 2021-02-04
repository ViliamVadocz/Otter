from math import pi
from typing import Any, Union, Callable, Optional

from utils import rendering
from move.drive import Drive
from utils.const import BOOST_ACC, MAX_CAR_SPEED
from utils.const import MAX_JUMP_HEIGHT as MAX_JUMP_HEIGHT_CONST
from utils.const import MAX_NO_BOOST_SPEED, jump_height_to_time
from utils.aiming import get_offset_direction
from utils.vectors import dist, flatten_by_normal
from utils.game_info import GameInfo
from move.strike.strike import Strike
from rlutilities.mechanics import Dodge
from rlutilities.simulation import Car, Ball
from rlutilities.linear_algebra import dot, norm, vec2, vec3, normalize, angle_between

OFFSET_DISTANCE: float = 130
MAX_BACKWARDS_DIST = 1000
MIN_BACKWARD_ANGLE = pi / 2 + 0.3


class DriveStrike(Strike):
    MIN_JUMP_HEIGHT: float = 0
    MAX_JUMP_HEIGHT: float = MAX_JUMP_HEIGHT_CONST + 60
    JUMP_HEIGHT_TO_TIME: Callable[[float], float] = jump_height_to_time

    def __init__(self, info: GameInfo, target: Ball, goal: vec2):
        super().__init__(info, target)
        self.target_position: vec3 = vec3(self.target.position)
        self.target_position += OFFSET_DISTANCE * vec3(
            get_offset_direction(info.car.position, target, goal)
        )
        self.drive: Drive = Drive(info, self.target_position)
        self.jump: Optional[Union[Dodge, Any]] = None

    def update(self):
        time_left: float = self.target.time - self.info.time

        super().update()
        if self.jump:
            if hasattr(self.jump, "step"):
                self.jump.step(self.info.dt)
            else:
                self.jump.update()
            self.controls = self.jump.controls
            if time_left < 1 / 15:
                self.finished = self.jump.finished
            return

        # Calculations.
        car_to_target = self.target_position - self.info.car.position
        height: float = dot(car_to_target, self.info.car.up())
        if not (
            self.__class__.MIN_JUMP_HEIGHT < height < self.__class__.MAX_JUMP_HEIGHT
        ):
            self.finished = True
        car_to_target_flat = flatten_by_normal(car_to_target, self.info.car.up())
        distance: float = norm(car_to_target_flat)
        distance -= self.info.car.hitbox_widths.x + self.info.car.hitbox_offset.x
        self.drive.target_speed = distance / max(1e-10, time_left)

        # Going backwards.
        if (
            self.drive.target_speed < MAX_NO_BOOST_SPEED
            and distance < MAX_BACKWARDS_DIST
            and angle_between(self.info.car.forward(), car_to_target_flat)
            > MIN_BACKWARD_ANGLE
        ):
            self.drive.target_speed *= -1.0

        self.drive.update()
        self.controls = self.drive.controls

        # Jump execution.
        if self.info.car.on_ground:
            current_velocity: float = dot(
                normalize(car_to_target_flat), self.info.car.velocity,
            )
            if abs(current_velocity * time_left - distance) < 30:
                time_to_height: float = self.__class__.JUMP_HEIGHT_TO_TIME(height)
                if time_to_height > 0.2 and time_left < time_to_height + 1 / 30:
                    self.start_jump(time_left)
                    return
        else:
            self.finished = True

        # Rendering.
        rendering.draw_line_3d(
            self.info.car.position,
            self.info.car.position + normalize(self.info.car.velocity) * distance,
            rendering.red(),
        )
        rendering.draw_line_3d(
            self.info.car.position,
            self.info.car.position + self.info.car.velocity * time_left,
            rendering.pink(),
        )
        rendering.draw_line_3d(
            self.target_position,
            self.target_position - height * self.info.car.up(),
            rendering.white(),
        )

    def start_jump(self, time_left: float):
        self.jump = Dodge(self.info.car)
        self.jump.jump_duration = 0.2
        self.jump.delay = max(1 / 60 + self.jump.jump_duration, time_left - 1 / 30,)
        self.jump.direction = vec2(self.target.position - self.target_position)
        self.jump.step(self.info.dt)
        self.controls = self.jump.controls

    @classmethod
    def valid_target(cls, car: Car, target: vec3, time: float) -> bool:
        height: float = dot(target - car.position, car.up())
        if not (cls.MIN_JUMP_HEIGHT < height < cls.MAX_JUMP_HEIGHT):
            return False
        t: float = max(1e-10, time - car.time)
        u: float = dot(
            car.velocity, normalize(target - car.position),
        )
        s: float = dist(target, car.position) - abs(height)
        return (2 * s) / t - u < 0.95 * max(
            MAX_NO_BOOST_SPEED, min(MAX_CAR_SPEED, abs(u) + car.boost / 33 * BOOST_ACC),
        )
