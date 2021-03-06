from math import pi, atan2, isinf
from typing import Any, Tuple, Union, Callable, Optional

from utils import rendering
from move.drive import Drive
from utils.const import (
    BOOST_ACC,
    BOOST_USAGE,
    MAX_CAR_SPEED,
    MAX_JUMP_DURATION,
    MAX_NO_BOOST_SPEED,
    MAX_FIRST_JUMP_HOLD,
)
from utils.aiming import get_offset_direction
from utils.vectors import dist, direction, flatten_by_normal
from utils.game_info import GameInfo
from move.strike.strike import Strike
from rlutilities.mechanics import Dodge
from utils.jump_prediction import solve_jump, time_to_reach_jump_height
from rlutilities.simulation import Car, Ball
from utils.drive_estimation import get_time_to_reach_distance
from rlutilities.linear_algebra import (
    xy,
    dot,
    norm,
    vec2,
    vec3,
    look_at,
    normalize,
    angle_between,
)

MAX_BACKWARDS_DIST = 1000
MAX_DIST_ERROR = 50


class JumpStrike(Strike):
    HEIGHT_OFFSET_DISTANCE: float = 50
    OFFSET_DISTANCE: float = Ball.collision_radius + 35
    SOLVE_JUMP: Callable[[Car, vec3, vec3], Tuple[vec3, float]] = solve_jump
    JUMP_HEIGHT_TO_TIME: Callable[
        [float, float, float], float
    ] = time_to_reach_jump_height

    def __init__(self, info: GameInfo, target: Ball, goal: vec3):
        super().__init__(info, target)
        self.target_position: vec3 = vec3(self.target.position)
        self.target_position += self.__class__.OFFSET_DISTANCE * vec3(
            get_offset_direction(info.car.position, target, xy(goal))
        )
        self.drive: Drive = Drive(info, self.target_position)
        self.jump: Optional[Union[Dodge, Any]] = None

    def update(self):
        car = self.info.car
        time_left: float = self.target.time - self.info.time

        super().update()
        if self.jump:
            rendering.draw_line_3d(
                car.position, self.target_position, rendering.yellow(),
            )
            if hasattr(self.jump, "step"):
                self.jump.step(self.info.dt)
            else:
                self.jump.update()
            self.controls = self.jump.controls
            if time_left < 1 / 15:
                self.finished = self.jump.finished
            return

        # Calculations.
        car_to_target = self.target_position - car.position
        height: float = max(
            0, dot(car_to_target, car.up()) - self.__class__.HEIGHT_OFFSET_DISTANCE
        )
        car_to_target_flat = flatten_by_normal(car_to_target, car.up())
        distance: float = norm(car_to_target_flat)
        distance -= car.hitbox_widths.x + car.hitbox_offset.x
        self.drive.target_speed = distance / max(1e-10, time_left)

        self.drive.update()
        self.controls = self.drive.controls

        # Jump execution.
        if self.info.car.on_ground:
            direction: float = dot(
                normalize(car_to_target_flat), normalize(self.info.car.velocity),
            )
            time_to_height: float = self.__class__.JUMP_HEIGHT_TO_TIME(
                height, dot(car.up(), self.info.gravity)
            )
            if (
                not isinf(time_to_height)
                and direction > 0.9
                and time_to_height > time_left - 1 / 60
            ):
                self.start_jump(time_left)
                return
        else:
            self.finished = True

        # Rendering.
        rendering.draw_line_3d(
            car.position,
            car.position + normalize(car.velocity) * distance,
            rendering.red(),
        )
        rendering.draw_line_3d(
            car.position, car.position + car.velocity * time_left, rendering.pink(),
        )
        rendering.draw_line_3d(
            self.target_position,
            self.target_position - height * car.up(),
            rendering.white(),
        )

    def start_jump(self, time_left: float):
        self.jump = Dodge(self.info.car)
        self.jump.jump_duration = 0.2
        self.jump.delay = max(1 / 60 + self.jump.jump_duration, time_left - 1 / 30,)
        end_car_position: vec3 = self.info.car.position + self.info.car.velocity * time_left + 0.5 * self.info.gravity * time_left ** 2
        dodge_direction: vec3 = direction(end_car_position, self.target.position)
        self.jump.direction = vec2(dodge_direction)
        self.jump.preorientation = look_at(vec3(0, 0, dodge_direction.z), vec3(0, 0, 1))
        self.jump.step(self.info.dt)
        self.controls = self.jump.controls

    @classmethod
    def valid_target(cls, info: GameInfo, car: Car, target: vec3, time: float) -> bool:
        local: vec3 = dot(car.orientation, target - car.position)
        height: float = max(0, local.z - cls.HEIGHT_OFFSET_DISTANCE)
        T = cls.JUMP_HEIGHT_TO_TIME(height, dot(car.up(), info.gravity))
        if isinf(T):
            return False

        s: float = norm(xy(local))
        u: float = dot(car.velocity, direction(car.position, target))
        t: float = (time - car.time - T)
        a: float = (2 * (s - u * (t + T))) / (t * (t + 2 * T))

        t2: float = get_time_to_reach_distance(s, max(0, u), car.boost)
        a2: float = (2 * (s - t2 * max(0, u))) / (t2 ** 2)

        angle: float = atan2(local.y, local.x)
        return (a2 * (0.8 - abs(angle) * 0.25)) > a and t2 < t + T
