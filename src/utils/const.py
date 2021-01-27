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
