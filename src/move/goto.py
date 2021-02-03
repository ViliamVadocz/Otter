from math import pi
from typing import Optional

from move.move import Move
from move.drive import Drive
from utils.const import MAX_CAR_SPEED, MAX_NO_BOOST_SPEED
from move.half_flip import HalfFlip
from move.speed_flip import SpeedFlip
from utils.game_info import GameInfo
from rlutilities.linear_algebra import dot, norm, vec3, normalize, angle_between

MIN_SPEED_FLIP_DIST = 2500
MIN_SPEED_FLIP_SPEED = 700
MAX_SPEED_FLIP_ANGLE = 0.3
MIN_HALF_FLIP_DIST = 800
MIN_HALF_FLIP_SPEED = 400
MIN_BACKWARD_ANGLE = pi / 2 + 0.3


class Goto(Move):
    def __init__(self, info: GameInfo, target: vec3):
        super().__init__(info)
        self.target = target
        self.drive = Drive(info, target)
        self.half_flip: Optional[HalfFlip] = None
        self.speed_flip: Optional[SpeedFlip] = None

    def update(self):
        car_to_target = self.target - self.info.car.position
        distance = norm(car_to_target)

        if self.half_flip is not None:
            self.half_flip.update()
            self.controls = self.half_flip.controls
            if self.half_flip.finished:
                self.half_flip = None
        elif self.speed_flip is not None:
            self.speed_flip.update()
            self.controls = self.speed_flip.controls
            if self.speed_flip.finished:
                self.speed_flip = None
        else:
            forward = self.info.car.forward()
            angle = angle_between(car_to_target, forward)
            forward_speed = dot(forward, self.info.car.velocity)
            grounded = (
                self.info.car.on_ground
                and dot(normalize(-1 * self.info.gravity), self.info.car.up()) > 0.8
            )
            if angle > MIN_BACKWARD_ANGLE:
                if (
                    grounded
                    and distance > MIN_HALF_FLIP_DIST
                    and forward_speed < -MIN_HALF_FLIP_SPEED
                ):
                    self.half_flip = HalfFlip(self.info)
                self.drive.target_speed = -MAX_NO_BOOST_SPEED
            else:
                if (
                    grounded
                    and distance > MIN_SPEED_FLIP_DIST
                    and forward_speed > MIN_SPEED_FLIP_SPEED
                    and angle < MAX_SPEED_FLIP_ANGLE
                ):
                    left: bool = dot(
                        self.target - self.info.car.position, self.info.car.left()
                    ) > 0
                    left = not left  # RLU is weird and left() is actually points right
                    self.speed_flip = SpeedFlip(self.info, spin_right=not left)
                self.drive.target_speed = MAX_CAR_SPEED
            self.drive.update()
            self.controls = self.drive.controls

        self.interruptible = self.half_flip is None and self.speed_flip is None
        self.finished = self.drive.finished  # and self.interruptible
