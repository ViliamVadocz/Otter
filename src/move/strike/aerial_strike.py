from typing import Optional

from utils import rendering
from move.drive import Drive
from move.aerial import Aerial
from utils.const import BOOST_ACC, BOOST_USAGE, MAX_CAR_SPEED, THROTTLE_ACC_IN_AIR
from utils.vectors import flatten_by_normal
from utils.game_info import GameInfo
from move.strike.strike import Strike
from rlutilities.simulation import Car, Ball, Field, sphere
from rlutilities.linear_algebra import dot, norm, vec3, normalize

MIN_BOOST = 70
OFFSET_DISTANCE = Ball.collision_radius + 20
MIN_BALL_DIST_FROM_FIELD = 400
MIN_CAR_DIST_FROM_FIELD = 300
MIN_TAKEOFF_SPEED = 500
MAX_FLAT_DISTANCE = 200


class AerialStrike(Strike):
    def __init__(self, info: GameInfo, target: Ball, goal: vec3):
        super().__init__(info, target)
        goal_to_ball = normalize(target.position - goal)
        self.target_position: vec3 = target.position + goal_to_ball * OFFSET_DISTANCE
        self.drive: Drive = Drive(info, self.target_position)
        self.jump: Optional[Aerial] = None

    def update(self):
        super().update()

        rendering.draw_line_3d(
            self.info.car.position, self.target_position, rendering.green(),
        )

        time_left = self.target.time - self.info.time
        if time_left < 0.0:
            self.finished = True

        if self.jump:
            self.jump.update()
            self.controls = self.jump.controls
            self.finished = self.jump.finished
            return

        if not self.info.car.on_ground:
            self.start_jump(time_left)
            self.jump = Aerial(self.info, self.target_position, self.target.time)
            self.jump.update()
            self.controls = self.jump.controls
            return

        car_to_target = flatten_by_normal(self.target_position, self.info.car.up())
        flat_distance = norm(car_to_target)
        # We don't want to aerial if the ball is right above us
        if flat_distance < MAX_FLAT_DISTANCE:
            self.finished = True

        self.drive.target_speed = norm(car_to_target) / max(1e10, time_left)
        self.drive.update()
        self.controls = self.drive.controls

        flat_vel: float = dot(
            normalize(car_to_target), self.info.car.velocity,
        )
        if abs(flat_vel * time_left - flat_distance) < 30:
            self.start_jump(time_left)

    def start_jump(self, time_left: float):
        self.jump = Aerial(self.info, self.target_position, self.target.time)
        self.jump.update()
        self.controls = self.jump.controls

    @classmethod
    def valid_target(cls, car: Car, target: vec3, time: float) -> bool:
        # Check that ball is far from ground, walls, and ceiling.
        collision_normal = Field.collide(
            sphere(target, MIN_BALL_DIST_FROM_FIELD)
        ).direction
        if norm(collision_normal) > 0.0:
            return False

        # If I am already in the air, check I am far from field.
        if not car.on_ground:
            collision_normal = Field.collide(
                sphere(target, MIN_CAR_DIST_FROM_FIELD)
            ).direction
            if norm(collision_normal) > 0.0:
                return False

        time_left = time - car.time
        car_to_target = target - car.position
        distance = norm(car_to_target)
        vel_in_dir = dot(car.velocity, normalize(car_to_target))
        max_boost_time = car.boost / BOOST_USAGE
        # TODO Get a better approximation, since not all the velocity is against gravity
        # TODO Use gravity from game_info, not hardcoded
        possible_vel_diff = (BOOST_ACC + THROTTLE_ACC_IN_AIR - 650) * min(
            time_left, max_boost_time
        )
        fastest_reachable = min(MAX_CAR_SPEED, vel_in_dir + possible_vel_diff)
        return distance / fastest_reachable < time_left
