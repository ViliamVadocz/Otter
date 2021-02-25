from typing import Any, Tuple, Union, Optional

from utils import rendering
from utils.const import MAX_CAR_SPEED
from utils.aiming import get_offset_direction
from utils.vectors import dist, direction, flatten_by_normal
from utils.game_info import GameInfo
from move.strike.strike import Strike
from move.directed_drive import DirectedDrive
from rlutilities.simulation import Car, Ball
from utils.drive_estimation import get_time_to_reach_distance
from rlutilities.linear_algebra import xy, dot, norm, vec3


class GroundStrike(Strike):
    def __init__(self, info: GameInfo, target: Ball, goal: vec3):
        super().__init__(info, target)
        self.target_position: vec3 = vec3(self.target.position)
        self.drive: DirectedDrive = DirectedDrive(
            info, self.target_position, direction(self.target_position, goal)
        )

    def update(self):
        super().update()

        car = self.info.car
        time_left: float = self.target.time - self.info.time
        if time_left < 0.0 or not car.on_ground:
            self.finished = True

        # Calculations.
        car_to_target = self.target_position - car.position
        car_to_target_flat = flatten_by_normal(car_to_target, car.up())
        distance: float = norm(car_to_target_flat)
        distance -= car.hitbox_widths.x + car.hitbox_offset.x
        distance += dist(car.position, self.drive.target) / 2
        self.drive.target_speed = distance / max(1e-10, time_left)

        self.drive.update()
        self.controls = self.drive.controls

        rendering.draw_line_3d(
            self.drive.target, self.target_position, rendering.yellow()
        )
        rendering.draw_rect_3d(self.target_position, 2, 2, True, rendering.red())

    @classmethod
    def valid_target(cls, info: GameInfo, car: Car, target: vec3, time: float) -> bool:
        # TODO Check if it is near a surface (and not on ceiling)
        # TODO Check if we can get to in time
        s = dist(car.position, target)
        d = direction(car.position, target)
        t = get_time_to_reach_distance(s, max(0, dot(d, car.velocity)), car.boost)
        return target.z < 100 and time - car.time > t
