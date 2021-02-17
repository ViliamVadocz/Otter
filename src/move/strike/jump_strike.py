from math import pi
from typing import Any, Tuple, Union, Callable, Optional

from utils import rendering
from move.drive import Drive
from utils.const import BOOST_ACC, BOOST_USAGE, MAX_CAR_SPEED
from utils.const import MAX_JUMP_HEIGHT as MAX_JUMP_HEIGHT_CONST
from utils.const import MAX_JUMP_DURATION, MAX_NO_BOOST_SPEED, MAX_FIRST_JUMP_HOLD
from utils.aiming import get_offset_direction
from utils.vectors import dist, direction, flatten_by_normal
from utils.game_info import GameInfo
from move.strike.strike import Strike
from rlutilities.mechanics import Dodge
from utils.jump_prediction import solve_jump
from rlutilities.simulation import Car, Ball
from rlutilities.linear_algebra import (
    xy,
    dot,
    norm,
    vec2,
    vec3,
    normalize,
    angle_between,
)

MAX_BACKWARDS_DIST = 1000
MIN_BACKWARD_ANGLE = pi / 2 + 0.3
MAX_DIST_ERROR = 30


class JumpStrike(Strike):
    OFFSET_DISTANCE: float = Ball.collision_radius + 35
    # TODO find min and max jump height using solver
    MIN_JUMP_HEIGHT: float = 0
    MAX_JUMP_HEIGHT: float = MAX_JUMP_HEIGHT_CONST + 60
    SOLVE_JUMP: Callable[[Car, vec3, vec3], Tuple[vec3, float]] = solve_jump

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
        height: float = dot(car_to_target, car.up())
        car_to_target_flat = flatten_by_normal(car_to_target, car.up())
        distance: float = norm(car_to_target_flat)
        distance -= car.hitbox_widths.x + car.hitbox_offset.x
        self.drive.target_speed = distance / max(1e-10, time_left)

        # If the target height is out of bounds, allow this move to be interrupted.
        self.interruptible = not (
            self.__class__.MIN_JUMP_HEIGHT * 0.95
            < height
            < self.__class__.MAX_JUMP_HEIGHT / 0.95
        )

        # Going backwards.
        if (
            self.drive.target_speed < MAX_NO_BOOST_SPEED
            and distance < MAX_BACKWARDS_DIST
            and angle_between(car.forward(), car_to_target_flat) > MIN_BACKWARD_ANGLE
        ):
            self.drive.target_speed *= -1.0

        self.drive.update()
        self.controls = self.drive.controls

        # Jump execution.
        if car.on_ground:
            offset, time_to_target = self.__class__.SOLVE_JUMP(
                car, self.info.gravity, self.target_position
            )
            rendering.draw_rect_3d(
                self.target_position + offset, 10, 10, True, rendering.green()
            )
            # TODO Use offset to adjust when jumping from walls.
            if norm(offset) < MAX_DIST_ERROR:
                if (
                    time_to_target > MAX_FIRST_JUMP_HOLD
                    and time_left < time_to_target + 1 / 30
                ):
                    if isinstance(self, JumpStrike):
                        if time_to_target < MAX_JUMP_DURATION:
                            self.start_jump(time_left)
                            return
                    else:
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
            car.velocity, direction(car.position, target),
        )
        s: float = dist(target, car.position) - abs(height)
        return (2 * s) / t - u < 0.95 * max(
            MAX_NO_BOOST_SPEED,
            min(MAX_CAR_SPEED, abs(u) + car.boost / BOOST_USAGE * BOOST_ACC),
        )
