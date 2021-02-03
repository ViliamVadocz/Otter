from math import pi
from typing import Optional

from utils import rendering
from move.drive import Drive
from utils.const import (
    BOOST_ACC,
    MAX_CAR_SPEED,
    MAX_JUMP_HEIGHT,
    MAX_NO_BOOST_SPEED,
    MAX_DOUBLE_JUMP_HEIGHT,
    double_jump_height_to_time,
)
from utils.aiming import get_offset_direction
from utils.vectors import flatten_by_normal_to_level
from utils.game_info import GameInfo
from move.double_jump import DoubleJump
from move.strike.strike import Strike
from rlutilities.simulation import Car, Ball
from move.strike.drive_strike import MAX_BACKWARDS_DIST, MIN_BACKWARD_ANGLE
from rlutilities.linear_algebra import (
    dot,
    norm,
    vec2,
    vec3,
    cross,
    normalize,
    angle_between,
)

OFFSET_DISTANCE: float = 70.0
MAX_VEL_DIFF = 200


class DoubleJumpStrike(Strike):
    def __init__(self, info: GameInfo, target: Ball, goal: vec2):
        super().__init__(info, target)
        self.target_position: vec3 = vec3(self.target.position)
        self.target_position += OFFSET_DISTANCE * vec3(
            get_offset_direction(info.car.position, target, goal)
        )
        self.drive: Drive = Drive(info, self.target_position)
        self.double_jump: Optional[DoubleJump] = None

    def update(self):
        time_left: float = self.target.time - self.info.time

        super().update()
        if self.double_jump:
            self.double_jump.update()
            self.controls = self.double_jump.controls
            return

        # Pretty much the same as DriveStrike.
        # Speed calculations.
        car_to__flat_target = flatten_by_normal_to_level(
            self.target_position - self.info.car.position,
            self.info.car.up(),
            self.info.car.position,
        )
        distance: float = norm(car_to__flat_target)
        distance -= self.info.car.hitbox_widths.x + self.info.car.hitbox_offset.x
        self.drive.target_speed = distance / max(1e-10, time_left)
        # Going backwards.
        if (
            self.drive.target_speed < MAX_NO_BOOST_SPEED
            and distance < MAX_BACKWARDS_DIST
            and angle_between(self.info.car.forward(), car_to__flat_target)
            > MIN_BACKWARD_ANGLE
        ):
            self.drive.target_speed *= -1.0

        self.drive.update()
        self.controls = self.drive.controls

        # Jump calculations.
        if self.info.car.on_ground:
            direction = normalize(car_to__flat_target)
            current_velocity: float = dot(
                direction, self.info.car.velocity,
            )
            if abs(current_velocity - self.drive.target_speed) < MAX_VEL_DIFF:
                height: float = dot(
                    self.target_position - self.info.car.position, self.info.car.up()
                )
                time_to_height: float = double_jump_height_to_time(height)
                rendering.draw_string_3d(
                    self.info.car.position,
                    2,
                    2,
                    f"{time_left - time_to_height:.2f}s",
                    rendering.red(),
                )
                if time_to_height > 0.2 and time_left < time_to_height:
                    self.double_jump = DoubleJump(self.info, self.target_position)
                    self.double_jump.update()
                    self.controls = self.double_jump.controls
                    self.controls.throttle = self.drive.controls.throttle
                    return
        else:
            self.finished = True

        rendering.draw_line_3d(
            self.info.car.position, self.target.position, rendering.green()
        )
        rendering.draw_rect_3d(self.target.position, 2, 2, True, rendering.green())

    @staticmethod
    def valid_target(car: Car, target: vec3, time: float):
        # TODO Put some more effort into this instead of just pinching r0bbi3's DriveStrike code.
        # TODO Make more aggressive.
        car_to_target = target - car.position
        height = dot(car.up(), car_to_target)
        if not (MAX_JUMP_HEIGHT < height < MAX_DOUBLE_JUMP_HEIGHT + 60):
            return False
        t: float = max(1e-10, time - car.time)
        u: float = dot(
            car.velocity, normalize(car_to_target),
        )
        s: float = norm(car_to_target) - abs(height)
        return (2 * s) / t - u < 0.95 * max(
            MAX_NO_BOOST_SPEED, min(MAX_CAR_SPEED, abs(u) + car.boost / 33 * BOOST_ACC),
        )
