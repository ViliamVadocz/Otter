from typing import Tuple, Optional

from utils import rendering
from move.drive import Drive
from move.aerial import Aerial
from utils.const import BOOST_ACC, BOOST_USAGE, MAX_CAR_SPEED, THROTTLE_ACC_IN_AIR
from utils.vectors import dist, direction, flatten_by_normal
from utils.game_info import GameInfo
from move.strike.strike import Strike
from rlutilities.mechanics import Aerial as RLUAerial
from rlutilities.simulation import Car, Ball, Field, sphere
from rlutilities.linear_algebra import dot, norm, vec3, normalize, angle_between

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
        self.target_position: vec3 = target.position + goal_to_ball * OFFSET_DISTANCE
        self.aerial_up: vec3 = -1 * goal_to_ball
        self.drive: Drive = Drive(info, self.target_position)
        self.jump: Optional[Aerial] = None

    def update(self):
        super().update()

        time_left = self.target.time - self.info.time
        if time_left < 0.0:
            self.finished = True

        sim_car, boost_estimate = self.simulate(Car(self.info.car))

        if self.jump:
            self.jump.update()
            self.controls = self.jump.controls
            self.finished = self.jump.finished
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
            self.info, self.target_position, self.target.time, self.aerial_up
        )
        self.jump.update()
        self.controls = self.jump.controls

    def simulate(self, sim_car: Car) -> Tuple[Car, float]:
        test_aerial = RLUAerial(sim_car)
        test_aerial.target_position = self.target_position
        test_aerial.arrival_time = self.target.time
        test_aerial.up = self.aerial_up

        DT = 1 / 120
        ticks = 0
        boost_used = 0.0
        while not test_aerial.finished:
            test_aerial.step(DT)
            sim_car.boost = 100
            sim_car.step(test_aerial.controls, DT)

            if test_aerial.controls.boost:
                boost_used += DT * BOOST_USAGE

            if ticks % 4 == 0:
                rendering.draw_rect_3d(sim_car.position, 5, 5, True, rendering.green())
            ticks += 1

        return sim_car, boost_used

    @classmethod
    def valid_target(cls, car: Car, target: vec3, time: float) -> bool:
        if car.boost < MIN_BOOST:
            return False
        time_left = time - car.time
        # Check that ball is far from ground, walls, and ceiling.
        collision_normal = Field.collide(
            sphere(target, MIN_BALL_DIST_FROM_FIELD)
        ).direction
        if norm(collision_normal) > 0.0:
            return False

        # If I am already in the air, check I am far from field.
        if not car.on_ground:
            collision_normal = Field.collide(
                sphere(car.position, MIN_CAR_DIST_FROM_FIELD)
            ).direction
            if norm(collision_normal) > 0.0:
                return False

        # TODO Make this actually make sense
        return (
            angle_between(car.forward(), direction(car.position, target)) < 0.7
            and dist(car.position, target) / 1500 < time_left
        )
