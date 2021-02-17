MAX_CAR_SPEED = 2300
MAX_NO_BOOST_SPEED = 1410
BOOST_ACC = 991.667
THROTTLE_ACC_IN_AIR = 66.66667
COAST_ACC = 525.0
BREAK_ACC = 3500
MIN_BOOST_TIME = 10 / 120
BOOST_USAGE = 100 / 3  # boost per sec

MAX_FIRST_JUMP_HOLD = 0.2
MAX_JUMP_DURATION = 1.25
JUMP_IMPULSE: float = 291.667
DOUBLE_JUMP_IMPULSE: float = JUMP_IMPULSE * 0.9162810719288189
JUMP_ACC: float = 1346.6605414091864
DODGE_IMPULSE: float = 500

DEFAULT_MAX_JUMP_HEIGHT: float = 220  # TODO Support variable gravity.
DEFAULT_MAX_DOUBLE_JUMP_HEIGHT: float = 440  # TODO Support variable gravity.


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
