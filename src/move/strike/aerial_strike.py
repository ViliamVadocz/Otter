from typing import Tuple, Optional

from utils import rendering
from move.drive import Drive
from move.aerial import Aerial
from utils.const import (
    JUMP_ACC,
    BOOST_ACC,
    BOOST_USAGE,
    JUMP_IMPULSE,
    DOUBLE_JUMP_IMPULSE,
    MAX_FIRST_JUMP_HOLD,
)
from utils.vectors import dist, up_at, direction, flatten_by_normal
from utils.game_info import GameInfo
from move.strike.strike import Strike
from rlutilities.mechanics import Aerial as RLUAerial
from utils.jump_prediction import predict_double_jump
from rlutilities.simulation import Car, Ball, Field, sphere
from rlutilities.linear_algebra import dot, mat3, norm, vec3, normalize, angle_between

OFFSET_DISTANCE = Ball.collision_radius + 20
SPEED_REDUCTANT = 300
MIN_BALL_DIST_FROM_FIELD = 500
MIN_CAR_DIST_FROM_FIELD = 300
MAX_DIST_ERROR = 50
MAX_ANGLE = 0.1
GIVE_UP_TIME = 0.6
MIN_BOOST = 30


class AerialStrike(Strike):
    def __init__(self, info: GameInfo, target: Ball, goal: vec3):
        super().__init__(info, target)
        goal_to_ball = direction(goal, target.position)
        self.target_position: vec3 = target.position + normalize(
            800 * goal_to_ball + info.gravity
        ) * OFFSET_DISTANCE
        self.aerial_orientation: vec3 = up_at(-1 * goal_to_ball, -1 * info.gravity)
        self.drive: Drive = Drive(info, self.target_position)
        self.jump: Optional[Aerial] = None

    def update(self):
        super().update()

        time_left = self.target.time - self.info.time
        if time_left < 0.0:
            self.finished = True

        sim_car = Car(self.info.car)
        sim_car, boost_estimate = self.simulate(
            sim_car,
            self.target_position,
            self.target.time,
            self.aerial_orientation,
            render=True,
        )

        if self.jump:
            self.jump.update()
            self.controls = self.jump.controls
            if self.jump.finished:
                self.finished = True
            rendering.draw_rect_3d(self.target_position, 8, 8, True, rendering.red())
            return

        if not self.info.car.on_ground:
            self.start_jump(time_left)
            return

        car_to_target = flatten_by_normal(
            self.target_position - self.info.car.position, self.info.car.up()
        )
        flat_distance = norm(car_to_target)

        self.drive.target_speed = max(0.0, flat_distance - SPEED_REDUCTANT) / max(
            1e-10, time_left
        )
        self.drive.update()
        self.controls = self.drive.controls

        # If still not in air, just give up.
        if time_left < GIVE_UP_TIME:
            self.finished = True
            return

        if (
            boost_estimate < self.info.car.boost
            and dist(sim_car.position, self.target_position) < MAX_DIST_ERROR
            and angle_between(self.info.car.forward(), car_to_target) < MAX_ANGLE
        ):
            self.start_jump(time_left)

    def start_jump(self, time_left: float):
        self.jump = Aerial(
            self.info, self.target_position, self.target.time, self.aerial_orientation
        )
        self.jump.update()
        self.controls = self.jump.controls

    @staticmethod
    def simulate(
        sim_car: Car,
        target_pos: vec3,
        arrival_time: float,
        orientation: mat3,
        render: bool = False,
    ) -> Tuple[Car, float]:
        test_aerial = RLUAerial(sim_car)
        test_aerial.target_position = target_pos
        test_aerial.arrival_time = arrival_time
        test_aerial.target_orientation = orientation
        test_aerial.double_jump = True

        DT = 1 / 120
        ticks = 0
        boost_used = 0.0
        while not test_aerial.finished:
            test_aerial.step(DT)
            sim_car.boost = 100
            sim_car.step(test_aerial.controls, DT)

            if test_aerial.controls.boost:
                boost_used += DT * BOOST_USAGE

            if render and ticks % 4 == 0:
                rendering.draw_rect_3d(sim_car.position, 5, 5, True, rendering.green())
            ticks += 1

        return sim_car, boost_used

    @classmethod
    def valid_target(cls, info: GameInfo, car: Car, target: vec3, time: float) -> bool:
        time_left = time - car.time

        goal: vec3 = info.goals[not info.car.team].position

        if not car.on_ground:
            distance = dist(car.position, target)
            if distance > 800:
                return False
            collision_normal = Field.collide(
                sphere(car.position, MIN_CAR_DIST_FROM_FIELD)
            ).direction
            if norm(collision_normal) > 0.0:
                return False

            # Simulate aerial
            sim_car, boost_used = cls.simulate(
                Car(car),
                target,
                time,
                up_at(direction(target, goal), -1 * info.gravity),
            )
            return (
                boost_used < car.boost
                and dist(sim_car.position, target) < MAX_DIST_ERROR
            )

        if car.boost < MIN_BOOST:
            return False
        # Check that ball is far from ground, walls, and ceiling.
        collision_normal = Field.collide(
            sphere(target, MIN_BALL_DIST_FROM_FIELD)
        ).direction
        if norm(collision_normal) > 0.0:
            return False

        # TODO Make this actually make sense
        car_to_target = target - car.position
        ground_time = norm(flatten_by_normal(car_to_target, car.up())) / 2000
        air_time = dot(car_to_target, normalize(-1 * info.gravity)) / 1200
        return (
            angle_between(car.forward(), direction(car.position, target)) < 0.7
            and ground_time + air_time < time_left
        )
