from math import pi, atan2, isinf
from typing import Any, Tuple, Union, Callable, Optional

from utils import rendering
from move.drive import Drive
from utils.const import (
    JUMP_ACC,
    BREAK_ACC,
    JUMP_IMPULSE,
    MAX_CAR_SPEED,
    DODGE_TIME_LIMIT,
    SUPERSONIC_SPEED,
    DEFAULT_JUMP_PEAK_TIME,
)
from utils.aiming import get_offset_direction
from utils.vectors import direction, flatten_by_normal
from utils.game_info import GameInfo
from move.strike.strike import Strike
from rlutilities.mechanics import Dodge
from utils.jump_prediction import solve_jump, time_to_reach_jump_height
from rlutilities.simulation import Car, Ball
from utils.drive_estimation import get_time_to_reach_distance
from rlutilities.linear_algebra import xy, dot, norm, vec2, vec3, look_at, normalize

MAX_BACKWARDS_DIST = 1000
MAX_DIST_ERROR = 50


class JumpStrike(Strike):
    HEIGHT_OFFSET_DISTANCE: float = 50
    OFFSET_DISTANCE: float = Ball.collision_radius + 35

    SOLVE_JUMP: Callable[[Car, vec3, vec3], Tuple[vec3, float]] = solve_jump
    JUMP_HEIGHT_TO_TIME: Callable[
        [float, float, float], float
    ] = time_to_reach_jump_height
    JUMP_PEAK_TIME: float = DEFAULT_JUMP_PEAK_TIME

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

        super().update()

        # Calculations.
        car_to_target = self.target_position - car.position
        height: float = max(0, dot(car_to_target, car.up()))
        car_to_target_flat = flatten_by_normal(car_to_target, car.up())
        distance: float = norm(car_to_target_flat)
        distance -= car.hitbox_widths.x + car.hitbox_offset.x
        time_to_height: float = self.__class__.JUMP_HEIGHT_TO_TIME(
            height, dot(car.up(), self.info.gravity)
        )
        if isinf(time_to_height):
            time_to_height = self.__class__.JUMP_PEAK_TIME
        self.drive.target = (
            self.target_position
            + 0.5
            * self.info.gravity
            * (0 if isinf(time_to_height) else time_to_height) ** 2
        )

        # Update drive.
        angle: float = atan2(
            dot(car.left(), car_to_target), dot(car.forward(), car_to_target)
        )
        if abs(angle) > pi / 16:
            self.drive.target_speed = 850
            self.drive.update()
            self.controls = self.drive.controls
        else:
            self.drive.update()
            self.controls = self.drive.controls

            u: float = dot(car.velocity, normalize(car_to_target_flat))
            break_throttle: float = (-u * 120) / BREAK_ACC
            if u >= 0:
                t: float = time_left - time_to_height
                s: float = norm(car_to_target_flat)
                d: float = (t * (s + time_to_height * max(0, u))) / (
                    t + 2 * time_to_height
                )

                # v: float = (2 * d) / t - u
                # if v > SUPERSONIC_SPEED and not car.supersonic:
                #     # Boost now to avoid boosting when supersonic later.
                #     self.controls.throttle = 1
                #     self.controls.boost = True
                # el
                if d >= 0:
                    t2: float = get_time_to_reach_distance(d, max(0, u), car.boost)
                    try:
                        throttle: float = 2 ** (10 * (t2 / t - 1))
                    except OverflowError:
                        throttle: float = 1
                    throttle = throttle * (1 - break_throttle) + break_throttle
                    self.controls.throttle = max(0, min(1, throttle))
                    self.controls.boost = throttle > 0.99 and u < MAX_CAR_SPEED - 5
            else:
                self.controls.throttle = max(0, min(1, break_throttle))
                self.controls.boost = break_throttle >= 1

        # Jump execution.
        if self.info.car.on_ground:
            direction: float = dot(
                normalize(car_to_target_flat), normalize(self.info.car.velocity),
            )
            if (
                not isinf(time_to_height)
                and direction > 0.9
                and time_to_height > time_left
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
        self.jump.delay = max(1 / 60 + self.jump.jump_duration, time_left,)

        self.jump.direction = vec2(self.target.position - self.target_position)
        self.jump.preorientation = look_at(self.info.car.velocity, vec3(0, 0, 1))

        self.jump.step(self.info.dt)
        self.controls = self.jump.controls

    @classmethod
    def valid_target(cls, info: GameInfo, car: Car, target: vec3, time: float) -> bool:
        height: float = max(
            0, dot(car.up(), target - car.position) - cls.HEIGHT_OFFSET_DISTANCE
        )
        T = cls.JUMP_HEIGHT_TO_TIME(height, dot(car.up(), info.gravity))
        if isinf(T) or T > DODGE_TIME_LIMIT:
            return False

        # Adjust destination for wall-hits.
        destination: vec3 = target
        destination += 0.5 * info.gravity * T ** 2
        local = dot(destination - car.position, car.orientation)

        # Specify conditions to be met.
        u: float = dot(car.velocity, direction(car.position, target))
        t: float = (time - car.time - T)
        angle: float = atan2(local.y, local.x)
        t -= max(0, u / -BREAK_ACC * 6)
        t -= abs(angle) * 0.37
        if t <= 0:
            return False
        s: float = norm(xy(local))
        d: float = (t * (s + T * max(0, u))) / (t + 2 * T)

        # Can we meet those conditions?
        t2: float = get_time_to_reach_distance(d, max(0, u), car.boost)
        return t2 < t
