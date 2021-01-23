from math import exp, atan2

from rlbot.utils.rendering.rendering_manager import RenderingManager

from move.move import Move
from utils.const import MAX_CAR_SPEED
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
        car = self.info.my_car
        car_to_target = self.target - car.position
        angle = atan2(dot(car.left(), car_to_target), dot(car.forward(), car_to_target))
        abs_angle = abs(angle)

        # TODO A proper speed controller.
        speed = norm(car.velocity)
        self.controls.throttle = 1.0 if speed < self.target_speed else 0.0
        self.controls.boost = (
            speed < self.target_speed
            and abs_angle < MAX_BOOST_ANGLE
            and speed < MAX_CAR_SPEED
        )
        self.controls.steer = 2 / (1 + exp(-5.0 * angle)) - 1
        self.controls.handbrake = abs_angle > HANDBRAKE_ANGLE

        self.finished = norm(car_to_target) < FINISHED_DIST

    def render(self, r: RenderingManager):
        r.draw_rect_3d(self.target, 3, 3, True, r.red())
        r.draw_line_3d(self.info.my_car.position, self.target, r.white())
