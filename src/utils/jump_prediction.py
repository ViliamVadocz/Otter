from math import inf, isnan
from typing import Any, Tuple, Optional, Collection

import numpy as np

from utils.const import JUMP_ACC, JUMP_IMPULSE, DOUBLE_JUMP_IMPULSE, MAX_FIRST_JUMP_HOLD
from utils.vectors import up_at
from rlutilities.simulation import Car
from rlutilities.linear_algebra import dot, norm, vec3, normalize


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


def get_roots(pos: vec3, vel: vec3, acc: vec3, target: vec3) -> Collection[Any]:
    # We want to find when the distance to target is smallest.
    # let f(t) = pos + vel * t + 0.5 * acc * time^2 - target
    # We find the minimum of ||f(t)||.
    # d(||f(t)||^2) / dt = 2 * f'(t) . f(t)
    # Set derivative equal to zero and you get a cubic in t.
    a = 0.5 * dot(acc, acc)
    b = 1.5 * dot(acc, vel)
    c = dot(vel, vel) + dot(acc, pos - target)
    d = dot(vel, pos - target)
    return np.roots([a, b, c, d])


def smallest_real_root_in_range(
    roots, minimum: float, maximum: float
) -> Optional[float]:
    best_time = None
    for root in roots:
        maybe_real = np.real_if_close(root)
        if (
            np.isreal(maybe_real)
            and minimum <= maybe_real < maximum
            and (best_time is None or maybe_real < best_time)
        ):
            best_time = maybe_real
    return best_time


def solve_jump(car: Car, grav: vec3, target: vec3) -> Tuple[vec3, float]:
    up = car.up()
    # Assume closest is after first jump. (time >= MAX_FIRST_JUMP_HOLD)
    pos = predict_jump(car, grav, MAX_FIRST_JUMP_HOLD)
    vel = (car.velocity + up * JUMP_IMPULSE) + (
        grav + up * JUMP_ACC
    ) * MAX_FIRST_JUMP_HOLD
    acc = grav
    roots = get_roots(pos, vel, acc, target)
    best_time = smallest_real_root_in_range(roots, -MAX_FIRST_JUMP_HOLD, inf)
    if best_time is None:
        best_time = inf
    else:
        best_time += MAX_FIRST_JUMP_HOLD
    return predict_jump(car, grav, best_time) - target, best_time


def solve_double_jump(car: Car, grav: vec3, target: vec3) -> Tuple[vec3, float]:
    up = car.up()
    # Assume closest is after first jump. (time >= MAX_FIRST_JUMP_HOLD)
    pos = predict_double_jump(car, grav, MAX_FIRST_JUMP_HOLD)
    vel = (car.velocity + up * (JUMP_IMPULSE + DOUBLE_JUMP_IMPULSE)) + (
        grav + up * JUMP_ACC
    ) * MAX_FIRST_JUMP_HOLD
    acc = grav
    roots = get_roots(pos, vel, acc, target)
    best_time = smallest_real_root_in_range(roots, -MAX_FIRST_JUMP_HOLD, inf)
    if best_time is None:
        best_time = inf
    else:
        best_time += MAX_FIRST_JUMP_HOLD
    return predict_double_jump(car, grav, best_time) - target, best_time


def get_jump_peak(grav: vec3) -> float:
    up = normalize(-1 * grav)
    target = up * 10000
    car = Car()
    car.orientation = up_at(up, vec3(1, 0, 0))
    offset, time_to_reach = solve_jump(car, grav, target)
    max_height = norm(offset + target)
    if isnan(max_height):
        return 10000
    return max_height, time_to_reach


def get_double_jump_peak(grav: vec3) -> float:
    up = normalize(-1 * grav)
    target = up * 10000
    car = Car()
    car.orientation = up_at(up, vec3(1, 0, 0))
    offset, time_to_reach = solve_double_jump(car, grav, target)
    max_height = norm(offset + target)
    if isnan(max_height):
        return 10000
    return max_height, time_to_reach
