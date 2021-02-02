MAX_CAR_SPEED = 2300
MAX_NO_BOOST_SPEED = 1410
BOOST_ACC = 991.667
COAST_ACC = 525.0
BREAK_ACC = 3500
MIN_BOOST_TIME = 10 / 120

MAX_FIRST_JUMP_HOLD = 0.2
MAX_JUMP_DURATION = 1.25
JUMP_IMPULSE = 291.667
JUMP_ACC = 1458.333374

MAX_JUMP_HEIGHT: float = 220  # TODO Support variable gravity.
MAX_DOUBLE_JUMP_HEIGHT: float = 440  # TODO Support variable gravity.


def throttle_acc_from_speed(speed):
    # https://samuelpmish.github.io/notes/RocketLeague/ground_control/#throttle
    if speed < 0:
        return BREAK_ACC
    if speed < 1400:
        return (-36 / 35) * speed + 1600
    elif speed < 1410:
        return -16 * speed + 22560
    else:
        return 0


def double_jump_height_to_time(x):
    # Hold for MAX_FIRST_JUMP_HOLD and then jump again right after.
    x = max(0, min(MAX_DOUBLE_JUMP_HEIGHT, x))
    a = 1.872348977e-8
    b = -1.126747937e-5
    c = 3.560647225e-3
    d = -7.446058499e-3
    return a * x ** 3 + b * x ** 2 + c * x + d


def jump_height_to_time(x):
    # Single jump estimation.
    x = max(0, min(MAX_JUMP_HEIGHT, x))
    a = 9.4343801054e-10
    b = -3.0870839992e-7
    c = 3.1466727477e-5
    d = 1.5970047137e-3
    e = 1.5706693469e-2
    return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e


def get_speed_from_radius(radius: float) -> float:
    curvature: float = 1 / max(1e-10, abs(radius))
    if curvature <= 0.00088:
        return 2300
    elif curvature <= 0.0011:
        return (curvature - 0.00088) / (0.0011 - 0.00088) * (1750 - 2300) + 2300
    elif curvature <= 0.001375:
        return (curvature - 0.0011) / (0.001375 - 0.0011) * (1500 - 1750) + 1750
    elif curvature <= 0.00235:
        return (curvature - 0.001375) / (0.00235 - 0.001375) * (1000 - 1500) + 1500
    elif curvature <= 0.00398:
        return (curvature - 0.00235) / (0.00398 - 0.00235) * (500 - 1000) + 1000
    else:
        return max(0, (curvature - 0.00398) / (0.0069 - 0.00398) * (0 - 500) + 500)
