from typing import Tuple, Optional

from utils import rendering
from move.move import Move
from utils.const import MAX_CAR_SPEED
from utils.vectors import dist
from utils.game_info import GameInfo
from rlutilities.mechanics import FollowPath
from rlutilities.simulation import Ball, Field, Navigator, sphere
from rlutilities.linear_algebra import norm

OFFSET = Ball.collision_radius + 50


class NavStrike(Move):
    def __init__(self, info: GameInfo, follow: FollowPath):
        super().__init__(info)
        self.follow = follow

    def update(self):
        self.follow.step(self.info.dt)
        self.controls = self.follow.controls
        self.finished = self.info.time > self.follow.arrival_time
        for ball in self.info.ball_prediction:
            if ball.time > self.follow.arrival_time:
                if dist(self.follow.path.points[-1], ball.position) > 200:
                    self.finished = True
                break

        rendering.draw_polyline_3d(self.follow.path.points, rendering.red())

    @staticmethod
    def plan_path(info: GameInfo) -> Optional[FollowPath]:
        print("PLANNING", end="")
        car = info.car
        nav = Navigator(car)
        nav.analyze_surroundings()
        follow = FollowPath(car)

        goal = info.goals[not car.team].position
        for ball in info.ball_prediction:
            if (
                dist(car.position, ball.position)
                > (ball.time - car.time) * MAX_CAR_SPEED
            ):
                continue

            # Check that the ball is close to field.
            collision_normal = Field.collide(
                sphere(
                    ball.position,
                    Ball.collision_radius + car.hitbox_widths.z + car.hitbox_widths.x,
                )
            ).direction
            if norm(collision_normal) == 0.0:
                continue

            # Calculate a drivable path.
            tangent = goal - ball.position
            curve = nav.path_to(ball.position, tangent, OFFSET)
            if len(curve.points) == 0:
                continue

            # Check if we can drive that path in time.
            for final_speed in range(MAX_CAR_SPEED - 100, 800, -100):
                print(".", end="")
                if follow.calculate_plan(curve, ball.time, final_speed):
                    print("")
                    return follow

        print("")
        return None
