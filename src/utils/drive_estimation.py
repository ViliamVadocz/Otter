from utils.const import BOOST_USAGE, MAX_CAR_SPEED, MAX_NO_BOOST_SPEED

_BOOST_DISTANCE: float = 2541.02001953125
_THROTTLE_DISTANCE: float = 1523.1700439453125


def _time_to_speed(speed: float, boost: bool) -> float:
    if boost:
        return (
            2620.2696820183323 * speed
            + -1368.2246940174318 * speed ** 2
            + 370.67380147518276 * speed ** 3
        )
    return (
        1568.3371768407985 * speed
        + -691.2054831674493 * speed ** 2
        + 126.01793019670737 * speed ** 3
    )


def _distance_to_time(time: float, boost: bool) -> float:
    if boost:
        return (
            time + 48.48140452579765
        ) ** 0.5 * 0.03858075642237755 + -0.20622521650405476
    return (
        time + 43.41414902262599
    ) ** 0.5 * 0.050975993945055816 + -0.2639051435040556


def _speed_to_distance(speed: float, boost: bool) -> float:
    if boost:
        return (
            -0.07267335021447095 * speed
            + 0.0002507343310505393 * speed ** 2
            + 9.794747003917977e-08 * speed ** 3
        )
    return (
        0.3564224344073551 * speed
        + -0.0008681746346982432 * speed ** 2
        + 1.105547777450585e-06 * speed ** 3
    )


def get_time_to_reach_distance(distance: float, start_speed: float, boost: float):
    assert distance >= 0
    assert start_speed >= 0
    assert 100 >= boost >= 0

    boost_time: float = boost / BOOST_USAGE

    boost_start_distance: float = _speed_to_distance(start_speed, True)
    boost_start_time: float = _distance_to_time(boost_start_distance, True)
    reach_max_speed: bool = _distance_to_time(
        _speed_to_distance(MAX_CAR_SPEED, True), True
    ) <= (boost_start_time + boost_time)

    # Reach max speed.
    if reach_max_speed:
        distance += boost_start_distance
        boost_max_time: float = max(0, distance - _BOOST_DISTANCE) / MAX_CAR_SPEED
        return (
            _distance_to_time(min(distance, _BOOST_DISTANCE), True)
            - boost_start_time
            + boost_max_time
        )

    # Run out of boost beyond throttle max speed.
    throttle_start_speed: float = _time_to_speed(boost_start_time + boost_time, True)
    if throttle_start_speed >= MAX_NO_BOOST_SPEED:
        distance += boost_start_distance - _speed_to_distance(
            throttle_start_speed, True
        )
        return boost_time + distance / throttle_start_speed

    # Reach throttle max speed.
    throttle_start_distance: float = _speed_to_distance(throttle_start_speed, False)
    throttle_start_time: float = _distance_to_time(throttle_start_distance, False)
    distance += throttle_start_distance
    throttle_to_max_time: float = _distance_to_time(
        min(_THROTTLE_DISTANCE, distance), False
    ) - throttle_start_time
    throttle_after_max_time: float = max(
        0, distance - _THROTTLE_DISTANCE
    ) / MAX_NO_BOOST_SPEED
    return boost_time + throttle_to_max_time + throttle_after_max_time


if __name__ == "__main__":
    from matplotlib.pyplot import plot, show

    data = []
    for speed in range(0, 2301, 2300 // 100):
        time: float = get_time_to_reach_distance(4600, speed, 100)
        print(str(speed) + "uu/s: " + str(round(time, 3)) + "s")
        data.append((speed, time))
    plot(*zip(*data))
    show()
