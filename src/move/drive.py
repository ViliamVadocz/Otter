from math import exp, atan2
from typing import Tuple

from rlbot.utils.rendering.rendering_manager import RenderingManager

from move.move import Move
from utils.const import (
    BOOST_ACC,
    BREAK_ACC,
    COAST_ACC,
    MAX_CAR_SPEED,
    MIN_BOOST_TIME,
    MAX_NO_BOOST_SPEED,
    throttle_acc_from_speed,
)
from utils.game_info import GameInfo
from rlutilities.linear_algebra import dot, norm, vec3

MAX_BOOST_ANGLE = 0.3
HANDBRAKE_ANGLE = 1.7
FINISHED_DIST = 100


class Drive(Move):
    def __init__(self, info: GameInfo, target: vec3):
        super().__init__(info)
        self.target = target
        self.target_speed = MAX_CAR_SPEED

    def update(self):
        car = self.info.car
        car_to_target = self.target - car.position
        angle = atan2(dot(car.left(), car_to_target), dot(car.forward(), car_to_target))
        abs_angle = abs(angle)

        # TODO A proper speed controller.
        speed = norm(car.velocity)
        self.controls.throttle, boost = speed_controller(
            speed, self.target_speed, self.info.dt
        )
        self.controls.boost = (
            boost and abs_angle < MAX_BOOST_ANGLE and speed < MAX_CAR_SPEED
        )
        self.controls.steer = 2 / (1 + exp(-5.0 * angle)) - 1
        self.controls.handbrake = abs_angle > HANDBRAKE_ANGLE

        self.finished = norm(car_to_target) < FINISHED_DIST

    def render(self, r: RenderingManager):
        r.draw_rect_3d(self.target, 3, 3, True, r.red())
        r.draw_line_3d(self.info.car.position, self.target, r.white())


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
