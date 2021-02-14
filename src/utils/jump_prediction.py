from utils.const import (
    JUMP_ACC,
    JUMP_IMPULSE,
    MAX_JUMP_DURATION,
    DOUBLE_JUMP_IMPULSE,
    MAX_FIRST_JUMP_HOLD,
)
from rlutilities.simulation import Car
from rlutilities.linear_algebra import vec3


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
        + (up * DOUBLE_JUMP_IMPULSE)  # second jump
    )
    fall_time = time - acc_time
    return pos + vel * fall_time + 0.5 * grav * fall_time * fall_time
