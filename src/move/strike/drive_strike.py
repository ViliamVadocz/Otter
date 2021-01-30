from math import pi
from typing import Optional

from utils import rendering
from move.drive import Drive
from utils.const import MAX_NO_BOOST_SPEED, jump_height_to_time
from utils.game_info import GameInfo
from move.strike.strike import Strike
from rlutilities.mechanics import Dodge
from rlutilities.simulation import Ball
from rlutilities.linear_algebra import (
    xy,
    dot,
    norm,
    vec2,
    vec3,
    normalize,
    angle_between,
)

OFFSET_DISTANCE: float = 115
MAX_BACKWARDS_DIST = 1000
MIN_BACKWARD_ANGLE = pi / 2 + 0.3


class DriveStrike(Strike):
    def __init__(self, info: GameInfo, target: Ball, goal: vec2):
        super().__init__(info, target)
        self.target_position: vec3 = vec3(self.target.position)
        self.target_position += (
            normalize(xy(self.target_position - goal)) * OFFSET_DISTANCE
        )
        self.drive: Drive = Drive(info, self.target_position)
        self.dodge: Optional[Dodge] = None

    def update(self):
        super().update()
        if self.dodge:
            self.finished = self.dodge.finished
            self.dodge.step(self.info.dt)
            self.controls = self.dodge.controls
            return

        # Speed calculations.
        car_to_target = self.target_position - self.info.car.position
        distance: float = norm(car_to_target)
        distance -= self.info.car.hitbox_widths.x + self.info.car.hitbox_offset.x
        self.drive.target_speed = distance / max(
            1e-10, self.target.time - self.info.time
        )
        # Going backwards.
        if (
            self.drive.target_speed < MAX_NO_BOOST_SPEED
            and distance < MAX_BACKWARDS_DIST
            and angle_between(self.info.car.forward(), car_to_target)
            > MIN_BACKWARD_ANGLE
        ):
            self.drive.target_speed *= -1.0

        self.drive.update()
        self.controls = self.drive.controls

        # Jump calculations.
        speed_accurate: bool = abs(
            norm(self.info.car.velocity) - self.drive.target_speed
        ) < 40
        if self.info.car.on_ground:
            if speed_accurate:
                height: float = dot(
                    self.target_position - self.info.car.position, self.info.car.up()
                )
                time_to_height: float = jump_height_to_time(height)
                if (
                    time_to_height > 0.2
                    and self.target.time - self.info.time < time_to_height + 1 / 60
                ):
                    self.dodge = Dodge(self.info.car)
                    self.dodge.jump_duration = 0.2
                    self.dodge.delay = max(
                        1 / 60 + self.dodge.jump_duration,
                        self.target.time - self.info.time,
                    )
                    self.dodge.direction = vec2(
                        self.target.position - self.info.car.position
                    )
                    self.dodge.step(self.info.dt)
                    self.controls = self.dodge.controls
                    self.finished = False
                    return
        else:
            self.finished = True

        rendering.draw_line_3d(
            self.info.car.position, self.target.position, rendering.green()
        )
        rendering.draw_rect_3d(self.target.position, 2, 2, True, rendering.green())
