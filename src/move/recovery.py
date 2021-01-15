from typing import Tuple

from move.move import Move
from utils.const import MAX_CAR_SPEED
from utils.game_info import GameInfo
from rlutilities.mechanics import AerialTurn
from rlutilities.simulation import Field, sphere
from rlutilities.linear_algebra import dot, mat3, norm, vec3, cross, normalize

SIM_POINTS_NUM = 200
SIM_DT = 1.0 / 30.0
SIM_SPHERE_R = 40


class Recovery(Move):
    def __init__(self, info: GameInfo):
        super().__init__(info)
        self.turn = AerialTurn(info.my_car)

    def update(self):
        _landing, orientation = self.simulate()
        # TODO boost towards ground
        self.turn.target = orientation
        self.turn.step(self.info.time_delta)
        self.controls = self.turn.controls
        self.finished = self.info.my_car.on_ground

    def simulate(self) -> Tuple[vec3, mat3]:
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
                return pos, orientation

        # If we don't return in the loop we use the current orientation.
        return pos, self.info.my_car.orientation
