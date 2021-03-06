from math import sqrt
from typing import Tuple

from utils import rendering
from move.move import Move
from utils.const import MAX_CAR_SPEED
from utils.vectors import dist, flatten_by_normal
from utils.game_info import GameInfo
from rlutilities.mechanics import ReorientML as Reorient
from rlutilities.simulation import Field, sphere
from rlutilities.linear_algebra import (
    dot,
    mat3,
    norm,
    vec3,
    cross,
    look_at,
    normalize,
    angle_between,
)

SIM_POINTS_NUM = 200
SIM_DT = 1.0 / 30.0
SIM_SPHERE_R = 40
BOOST_DOWN_TIME: float = 0.3
LOOK_DOWN_TIME: float = 0.6
MAX_BOOST_ANGLE: float = 0.4


class Recovery(Move):
    def __init__(self, info: GameInfo):
        super().__init__(info)
        self.reorient = Reorient(info.car)

    def update(self):
        car = self.info.car
        landing, orientation, normal, time = self.simulate()

        # Look down and boost.
        if car.boost and time > LOOK_DOWN_TIME:
            # Boost in opposite direction to normal
            # such that up is velocity flatted by normal.
            up = normalize(flatten_by_normal(car.velocity, normal))
            orientation = look_at(-1 * normal, up)
        self.controls.boost = (
            time > BOOST_DOWN_TIME
            and angle_between(car.orientation, orientation) < MAX_BOOST_ANGLE
        )

        self.reorient.target_orientation = orientation
        self.reorient.step(self.info.dt)
        self.controls.pitch = self.reorient.controls.pitch
        self.controls.yaw = self.reorient.controls.yaw
        self.controls.roll = self.reorient.controls.roll
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
        pos = vec3(self.info.car.position)
        vel = vec3(self.info.car.velocity)

        for i in range(SIM_POINTS_NUM):
            vel += self.info.gravity * SIM_DT
            vel /= max(1.0, norm(vel) / MAX_CAR_SPEED)
            pos += vel * SIM_DT

            rendering.draw_rect_3d(pos, 5, 5, True, rendering.blue())

            # Check for collisions with field.
            collision_normal = Field.collide(sphere(pos, SIM_SPHERE_R)).direction
            # Break out of simulation when collided.
            if norm(collision_normal) > 0.0:
                # Flatten velocity with regards to normal to get forward.
                forward = normalize(flatten_by_normal(vel, collision_normal))
                left = cross(collision_normal, forward)
                # fmt: off
                orientation = mat3(
                    forward[0], left[0], collision_normal[0],
                    forward[1], left[1], collision_normal[1],
                    forward[2], left[2], collision_normal[2],
                )
                # fmt: on
                return pos, orientation, collision_normal, SIM_DT * i

        # If we don't return in the loop, assume we will follow a parabola and land on flat-ground at z=0.
        time: float = -(
            sqrt(
                2
                * self.info.gravity.z
                * (self.info.car.hitbox_widths.z - self.info.car.position.z)
                + self.info.car.velocity.z ** 2
            )
            + self.info.car.velocity.z
        ) / self.info.gravity.z
        pos: vec3 = self.info.car.position + self.info.car.velocity * time + 0.5 * self.info.gravity * time ** 2
        vel: vec3 = self.info.car.velocity + self.info.gravity * time
        collision_normal: vec3 = vec3(0, 0, 1)
        # Flatten velocity with regards to normal to get forward.
        forward = normalize(flatten_by_normal(vel, collision_normal))
        left = cross(collision_normal, forward)
        # fmt: off
        orientation = mat3(
            forward[0], left[0], collision_normal[0],
            forward[1], left[1], collision_normal[1],
            forward[2], left[2], collision_normal[2],
        )
        # fmt: on
        return pos, orientation, collision_normal, time
