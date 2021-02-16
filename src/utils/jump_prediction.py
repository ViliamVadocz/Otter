from math import inf
from typing import Tuple

import numpy as np

from utils.const import JUMP_ACC, JUMP_IMPULSE, DOUBLE_JUMP_IMPULSE, MAX_FIRST_JUMP_HOLD
from rlutilities.simulation import Car
from rlutilities.linear_algebra import dot, vec3


def predict_jump(car: Car, grav: vec3, time: float) -> vec3:
    up = car.up()
    acc_time = min(time, MAX_FIRST_JUMP_HOLD)
    pos = (
        car.position
        + (car.velocity + up * JUMP_IMPULSE) * acc_time
        + 0.5 * (grav + up * JUMP_ACC) * acc_time * acc_time
    )
    if time <= MAX_FIRST_JUMP_HOLD:
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
    if time <= MAX_FIRST_JUMP_HOLD:
        return pos
    vel = (
        (car.velocity + up * JUMP_IMPULSE)
        + (grav + up * JUMP_ACC) * acc_time
        + (up * DOUBLE_JUMP_IMPULSE)  # second jump
    )
    fall_time = time - acc_time
    return pos + vel * fall_time + 0.5 * grav * fall_time * fall_time


def solve_jump(car: Car, grav: vec3, target: vec3) -> Tuple[vec3, float]:
    up = car.up()
    # Assume closest is after first jump. (time >= MAX_FIRST_JUMP_HOLD)
    pos = predict_jump(car, grav, MAX_FIRST_JUMP_HOLD)
    vel = (car.velocity + up * JUMP_IMPULSE) + (
        grav + up * JUMP_ACC
    ) * MAX_FIRST_JUMP_HOLD
    acc = grav

    # We want to find when the distance to target is smallest,
    # we find the minimum of f(t).
    # f(t) = pos + vel * t + 0.5 * acc * time^2 - target
    # d(||f(t)||^2) / dt = 2 * f'(t) . f(t)
    # Set derivative equal to zero and you get a cubic in t:
    a = 0.5 * dot(acc, acc)
    b = 1.5 * dot(acc, vel)
    c = dot(vel, vel) + dot(acc, pos - target)
    d = dot(vel, pos - target)

    # Find smallest real time which is >= 0.0.
    roots = np.roots([a, b, c, d])
    best_time = inf
    for root in roots:
        maybe_real = np.real_if_close(root)
        if np.isreal(maybe_real):
            maybe_real += MAX_FIRST_JUMP_HOLD
            if 0.0 <= maybe_real < best_time:
                best_time = maybe_real
    return predict_jump(car, grav, best_time) - target, best_time
