from math import inf

from utils import rendering
from move.move import Move
from move.drive import Drive
from utils.vectors import flatten_by_normal_to_level
from utils.game_info import GameInfo
from rlutilities.mechanics import Aerial as RLUAerial
from rlutilities.simulation import Input
from rlutilities.linear_algebra import dot, norm, vec3, normalize, angle_between

MAX_SPEED_ERROR = 0.3
SPEED_SUBTRACTANT = 300  # @r0bbi3 pls help rename this
MAX_JUMP_ANGLE = 0.1
GIVE_UP_SPEED = 2000


FIRST_JUMP = 0.15
BETWEEN_JUMPS = 0.1
SECOND_JUMP = 0.05


class Aerial(Move):
    def __init__(self, info: GameInfo, target: vec3, arrival_time: float):
        super().__init__(info)

        self.target = target
        self.arrival_time = arrival_time
        self.in_air = False
        self.jumped = False
        self.jump_timer = 0.0

        self.aerial = RLUAerial(self.info.car)
        self.aerial.target_position = self.target
        self.aerial.arrival_time = arrival_time

        self.drive = Drive(
            self.info,
            # TODO project down to ground instead of flat 20
            vec3(target[0], target[1], 20),
        )

    def update(self):

        if self.in_air:
            self.aerial.step(self.info.dt)
            self.controls = self.aerial.controls
            self.finished = (
                self.aerial.finished
                or self.info.car.on_ground
                or self.info.time > self.arrival_time
            )

        elif self.jumped:
            self.controls = Input()
            self.controls.throttle = 1.0
            self.controls.boost = True
            if self.jump_timer < FIRST_JUMP:
                self.controls.pitch = 1.0
                self.controls.jump = True
            elif self.jump_timer < FIRST_JUMP + BETWEEN_JUMPS:
                self.controls.pitch = 1.0
                self.controls.jump = False
            elif self.jump_timer < FIRST_JUMP + BETWEEN_JUMPS + SECOND_JUMP:
                self.controls.pitch = 0.0
                self.controls.jump = True
            else:
                self.in_air = True

            self.jump_timer += self.info.dt

        else:
            car = self.info.car
            time_left = self.arrival_time - self.info.time
            flat_displacement = flatten_by_normal_to_level(
                self.target - car.position, car.up(), car.position
            )
            speed_needed = norm(flat_displacement) / time_left - SPEED_SUBTRACTANT
            flat_vel = flatten_by_normal_to_level(car.velocity, car.up(), car.position)
            speed_in_direction = dot(normalize(flat_displacement), flat_vel)

            self.drive.target_speed = speed_needed
            self.drive.update()
            self.controls = self.drive.controls

            if speed_needed > GIVE_UP_SPEED or time_left < 0.0:
                self.finished = True
            elif (
                (speed_in_direction - speed_needed) / speed_needed < MAX_SPEED_ERROR
                and angle_between(flat_vel, flat_displacement) < MAX_JUMP_ANGLE
            ):
                self.jumped = True

        if self.in_air:
            rendering.draw_rect_3d(self.target, 3, 3, True, rendering.red())
            rendering.draw_line_3d(
                self.info.car.position, self.target, rendering.white()
            )
