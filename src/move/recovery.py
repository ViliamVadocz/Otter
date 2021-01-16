from typing import Tuple

from move.move import Move
from utils.const import MAX_CAR_SPEED
from utils.game_info import GameInfo
from rlutilities.mechanics import AerialTurn
from rlutilities.simulation import Field, sphere
from rlutilities.linear_algebra import (
    dot,
    mat3,
    norm,
    vec2,
    vec3,
    cross,
    look_at,
    normalize,
    angle_between,
)

SIM_POINTS_NUM = 200
SIM_DT = 1.0 / 30.0
SIM_SPHERE_R = 40
LOOK_DOWN_TIME = 0.6
MAX_BOOST_ANGLE = 0.1
MIN_BOOST = 0
MIN_LANDING_DIST = 300


class Recovery(Move):
    def __init__(self, info: GameInfo):
        super().__init__(info)
        self.turn = AerialTurn(info.my_car)

    def update(self):
        car = self.info.my_car
        landing, orientation, normal, time = self.simulate()

        boost = False
        if (
            car.boost > MIN_BOOST
            and time > LOOK_DOWN_TIME
            and norm(landing - car.position) > MIN_LANDING_DIST
        ):
            if normal is not None:
                # Boost in opposite direction to normal
                # such that up is velocity flatted by normal.
                up = normalize(car.velocity - dot(car.velocity, normal) * normal)
                orientation = look_at(-1 * normal, up)
            else:
                # Just boost down if we don't have a collision normal.
                flat_vel = car.velocity
                flat_vel[2] = 0
                orientation = look_at(vec3(0, 0, -1), normalize(flat_vel))

            boost = (
                norm(car.velocity) < 2300
                and angle_between(car.orientation, orientation) < MAX_BOOST_ANGLE
            )

        self.turn.target = orientation
        self.turn.step(self.info.time_delta)
        self.controls = self.turn.controls

        self.controls.boost = boost
        self.controls.throttle = 1.0  # Prevent turtling.

        # Jump when touching ceiling.
        upside_down = dot(car.up(), vec3(0, 0, 1)) < -0.7
        if upside_down:
            if car.on_ground:
                # Just spam jump. More elaborate solutions were less reliable.
                self.controls.jump = not self.controls.jump
        else:
            self.controls.jump = False

        self.finished = car.on_ground and not upside_down

    def simulate(self) -> Tuple[vec3, mat3, vec3, float]:
        pos = vec3(self.info.my_car.position)
        vel = vec3(self.info.my_car.velocity)
        grav = vec3(0, 0, 1) * self.info.gravity

        for i in range(SIM_POINTS_NUM):
            vel += grav * SIM_DT
            vel /= max(1.0, norm(vel) / MAX_CAR_SPEED)
            pos += vel * SIM_DT

            # Ignore initial frames in case of ceiling.
            if i < 5:
                self.info.draw.draw_rect_3d(pos, 5, 5, True, self.info.draw.purple())
                continue
            self.info.draw.draw_rect_3d(pos, 5, 5, True, self.info.draw.green())

            # Check for collisions with field.
            collision_normal = Field.collide(sphere(pos, SIM_SPHERE_R)).direction
            # Break out of simulation when collided.
            if norm(collision_normal) > 0.0:
                # Flatten velocity with regards to normal to get forward.
                forward = normalize(vel - dot(vel, collision_normal) * collision_normal)
                left = cross(collision_normal, forward)
                # fmt: off
                orientation = mat3(
                    forward[0], left[0], collision_normal[0],
                    forward[1], left[1], collision_normal[1],
                    forward[2], left[2], collision_normal[2],
                )
                # fmt: on
                return pos, orientation, collision_normal, SIM_DT * i

        # If we don't return in the loop we use the current orientation.
        return pos, self.info.my_car.orientation, None, SIM_POINTS_NUM * SIM_DT
