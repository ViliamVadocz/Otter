from utils.const import JUMP_ACC, JUMP_IMPULSE, MAX_JUMP_DURATION, MAX_FIRST_JUMP_HOLD
from rlutilities.simulation import Car
from rlutilities.linear_algebra import vec3


# Outdated, might delete
class Sim:
    def __init__(self, gravity=-650.0):
        self.g = gravity
        self.pos = 0.0
        self.vel = 0.0
        self.jump_time = 0.0
        self.jumps = 0

    def step(self, dt, jump):
        if self.jump_time > 0.0:
            self.jump_time += dt

        if jump:
            if self.jumps == 0:
                if self.jump_time == 0.0:
                    self.vel += JUMP_IMPULSE
                    self.jump_time += dt
                elif self.jump_time < MAX_FIRST_JUMP_HOLD:
                    self.vel += JUMP_ACC * dt
            elif self.jumps == 1 and self.jump_time < MAX_JUMP_DURATION:
                self.vel += JUMP_IMPULSE
                self.jumps = 2
        elif self.jumps == 0 and self.jump_time > 0.0:
            self.jumps += 1

        self.vel += self.g * dt
        self.pos += self.vel * dt

        if self.pos < 0.0:
            self.__init__(self.g)


def predict_jump(car: Car, grav: vec3, time: float) -> vec3:
    up = car.up()
    acc_time = min(time, MAX_FIRST_JUMP_HOLD)
    pos = (
        car.position
        + (car.velocity + up * JUMP_IMPULSE) * acc_time
        + 0.5 * (grav + up * JUMP_ACC) * acc_time * acc_time
    )
    if time < MAX_FIRST_JUMP_HOLD:
        return pos
    vel = (car.velocity + up * JUMP_IMPULSE) + (grav + up * JUMP_ACC) * acc_time
    fall_time = time - acc_time
    return pos + vel * fall_time + 0.5 * grav * fall_time * fall_time


def predict_double_jump(car: Car, grav: vec3, time: float) -> vec3:
    up = car.up()
    acc_time = min(time, MAX_FIRST_JUMP_HOLD)
    pos = (
        car.position
        + (car.velocity + up * JUMP_IMPULSE) * acc_time
        + 0.5 * (grav + up * JUMP_ACC) * acc_time * acc_time
    )
    if time < MAX_FIRST_JUMP_HOLD:
        return pos
    vel = (
        (car.velocity + up * JUMP_IMPULSE)
        + (grav + up * JUMP_ACC) * acc_time
        + (up * JUMP_IMPULSE * 0.9)  # second jump
    )
    fall_time = time - acc_time
    return pos + vel * fall_time + 0.5 * grav * fall_time * fall_time
