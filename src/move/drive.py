from math import pi, exp, atan2
from typing import Tuple

from utils import rendering
from move.move import Move
from utils.const import (
    BOOST_ACC,
    BREAK_ACC,
    COAST_ACC,
    MAX_CAR_SPEED,
    MIN_BOOST_TIME,
    MAX_NO_BOOST_SPEED,
    get_speed_from_radius,
    throttle_acc_from_speed,
)
from utils.game_info import GameInfo
from rlutilities.linear_algebra import dot, sgn, norm, vec3, normalize

MAX_BOOST_ANGLE = 0.3
HANDBRAKE_ANGLE = 1.5
HANDBRAKE_SPEED_RANGE = (800, 1400)
DEFAULT_FINISHED_DIST: float = 140


class Drive(Move):
    def __init__(
        self, info: GameInfo, target: vec3, finished_dist: float = DEFAULT_FINISHED_DIST
    ):
        super().__init__(info)
        self.target = target
        self.target_speed: float = MAX_CAR_SPEED
        self.finished_dist: float = finished_dist

    def update(self):
        car = self.info.car
        car_to_target = self.target - car.position
        angle = atan2(dot(car.left(), car_to_target), dot(car.forward(), car_to_target))
        if self.target_speed < 0:
            angle = sgn(angle) * (pi - abs(angle))
        abs_angle = abs(angle)

        # Clamp speed to maximum speed available due to target radius.
        local_radius: vec3 = dot(car.orientation, self.target - car.position)
        max_speed: float = abs(self.target_speed)
        for inaccuracy_sign in (-1, 2, 1):
            radius: float = (local_radius.x ** 2 + local_radius.y ** 2) / (
                2
                * max(
                    1e-10,
                    abs(local_radius.y) + inaccuracy_sign * self.finished_dist / 2,
                )
            )
            max_speed: float = max(max_speed, get_speed_from_radius(radius))
        desired_speed: float = max(-max_speed, min(max_speed, self.target_speed))

        speed = norm(car.velocity)
        throttle, boost = speed_controller(speed, desired_speed, self.info.dt)
        # Prevent wall slipping.
        on_wall = dot(self.info.car.up(), normalize(-1 * self.info.gravity)) < 0.7
        if on_wall and abs(throttle) < 0.05:
            throttle = 0.05 * sgn(desired_speed - speed)
        self.controls.throttle = throttle
        self.controls.boost = (
            boost and abs_angle < MAX_BOOST_ANGLE and speed < MAX_CAR_SPEED
        )

        # Steering.
        self.controls.steer = 2 / (1 + exp(-5.0 * angle)) - 1
        self.controls.handbrake = (
            abs_angle > HANDBRAKE_ANGLE
            and HANDBRAKE_SPEED_RANGE[0] < speed < HANDBRAKE_SPEED_RANGE[1]
            and not on_wall
        )
        if self.controls.handbrake:
            if dot(car.velocity, car.forward()) * self.target_speed < 0:
                self.controls.handbrake = False
            if dot(car.angular_velocity, car.up()) * angle * self.target_speed < 0:
                self.controls.handbrake = False

        self.finished = norm(car_to_target) < self.finished_dist

        rendering.draw_rect_3d(self.target, 3, 3, True, rendering.red())
        rendering.draw_line_3d(self.info.car.position, self.target, rendering.white())


def speed_controller(
    current_vel: float, desired_vel: float, dt: float
) -> Tuple[float, bool]:
    throttle = 0.02
    boost = False

    if dt <= 0.0:
        return throttle, boost

    desired_vel = max(-MAX_NO_BOOST_SPEED, min(MAX_CAR_SPEED, desired_vel))
    dv = desired_vel - current_vel
    desired_acc = dv / dt

    if desired_vel >= 0.0:
        throttle_acc = throttle_acc_from_speed(current_vel)

        if dv > (throttle_acc + BOOST_ACC) * MIN_BOOST_TIME:
            throttle = 1.0
            boost = True
        elif desired_acc >= throttle_acc:
            throttle = 1.0
        elif 0 < desired_acc:
            throttle = desired_acc / throttle_acc
        elif -COAST_ACC < desired_acc:
            pass
        elif -BREAK_ACC < desired_acc:
            throttle = 0.0
        else:
            throttle = -1.0

    else:
        throttle_acc = -throttle_acc_from_speed(-current_vel)

        if desired_acc <= throttle_acc:
            throttle = -1.0
        elif 0 > desired_acc:
            throttle = -desired_acc / throttle_acc
        elif COAST_ACC > desired_acc:
            throttle = -0.02
        elif BREAK_ACC > desired_acc:
            throttle = 0.0
        else:
            throttle = 1.0

    return throttle, boost
