from math import pi, exp, atan2
from typing import Tuple, Optional

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
HANDBRAKE_ANGLE = 1
HANDBRAKE_ANGLE_SPEED: float = 1.5
DEFAULT_FINISHED_DIST: float = 140


class Drive(Move):
    def __init__(
        self,
        info: GameInfo,
        target: vec3,
        finished_dist: float = DEFAULT_FINISHED_DIST,
        find_intermediate: bool = True,
        use_boost: bool = True,
    ):
        super().__init__(info)
        self.target = target
        self.target_speed: float = MAX_CAR_SPEED
        self.finished_dist: float = finished_dist
        self.find_intermediate: bool = find_intermediate
        self.use_boost: bool = use_boost

    def update(self):
        car = self.info.car

        # Find intermediate target.
        target: vec3 = self.target
        if self.find_intermediate:
            intermediate_target: Optional[vec3] = self.info.arena.find_intermediate(
                car.position, target
            )
            if intermediate_target:
                rendering.draw_polyline_3d(
                    [car.position, target, intermediate_target], rendering.cyan()
                )
                target = intermediate_target

        car_to_target: vec3 = target - car.position
        local_target: vec3 = dot(car_to_target, car.orientation)
        angle_velocity: float = dot(car.up(), car.angular_velocity)

        # Angle to target.
        angle: float = atan2(local_target.y, local_target.x)
        if self.target_speed < 0:
            angle = sgn(angle) * (pi - abs(angle))
        self.target_speed = abs(self.target_speed)

        # Clamp speed to maximum speed available due to target radius.
        local_radius: vec3 = dot(car.orientation, target - car.position)
        max_speed: float = abs(self.target_speed)
        for inaccuracy_sign in (-1, 2, 1):
            radius: float = (local_radius.x ** 2 + local_radius.y ** 2) / (
                2
                * max(
                    1e-10,
                    abs(local_radius.y) + inaccuracy_sign * self.finished_dist * 0.25,
                )
            )
            max_speed: float = max(max_speed, get_speed_from_radius(radius))
        desired_speed: float = max(-max_speed, min(max_speed, self.target_speed))

        # Throttle and boost.
        speed = norm(car.velocity)
        throttle, boost = speed_controller(speed, desired_speed, self.info.dt)
        on_wall = dot(self.info.car.up(), normalize(-1 * self.info.gravity)) < 0.7
        if on_wall and abs(throttle) < 0.05:
            throttle = 0.05 * sgn(desired_speed - speed)
        self.controls.throttle = throttle
        self.controls.boost = (
            boost
            and abs(angle) < MAX_BOOST_ANGLE
            and speed < MAX_CAR_SPEED
            and self.use_boost
        )

        # Steering.
        self.controls.steer = 250 * (angle - angle_velocity / 60) ** 3
        self.controls.steer = max(-1, min(1, self.controls.steer))
        self.controls.handbrake = (
            abs(angle) > HANDBRAKE_ANGLE
            and abs(angle_velocity) > HANDBRAKE_ANGLE_SPEED
            and not on_wall
        )
        if self.controls.handbrake:
            if dot(car.velocity, car.forward()) * self.target_speed < 0:
                self.controls.handbrake = False
            if angle * angle_velocity < 0:
                self.controls.handbrake = False

        self.finished = norm(car_to_target) < self.finished_dist

        rendering.draw_rect_3d(target, 3, 3, True, rendering.red())
        rendering.draw_line_3d(self.info.car.position, target, rendering.white())


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
