import sys
from math import sin, sqrt

import matplotlib.pyplot as plt

sys.path.insert(1, "../src")

from move.drive import speed_controller as drive_speed_controller
from utils.const import (
    BOOST_ACC,
    BREAK_ACC,
    COAST_ACC,
    BOOST_USAGE,
    MAX_CAR_SPEED,
    MIN_BOOST_TIME,
    throttle_acc_from_speed,
)


class Sim:
    def __init__(self):
        self.vel = 0.0
        self.boosting = False
        self.boost_time = 0.0
        self.boost_use = 0.0

    def step(self, dt, throttle, boost):
        throttle = max(-1.0, min(1.0, throttle))
        acc = 0.0

        if boost:
            self.boosting = True
        elif self.boost_time > MIN_BOOST_TIME:
            self.boosting = False
            self.boost_time = 0.0

        if self.boosting:
            throttle = 1.0
            acc += BOOST_ACC
            self.boost_time += dt
            self.boost_use += dt

        if throttle > 0.0:
            if self.vel < 0.0:
                acc += BREAK_ACC
            else:
                acc += throttle_acc_from_speed(self.vel) * throttle
        elif throttle < 0.0:
            if self.vel > 0.0:
                acc += -BREAK_ACC
            else:
                acc += throttle_acc_from_speed(-self.vel) * throttle
        else:
            if self.vel > 0.0:
                acc += -COAST_ACC
            elif self.vel < 0.0:
                acc += COAST_ACC

        self.vel += acc * dt
        self.vel = max(-MAX_CAR_SPEED, min(MAX_CAR_SPEED, self.vel))

    @property
    def boost_used(self):
        return self.boost_use * BOOST_USAGE


if __name__ == "__main__":
    # Replace with your own speed controller!
    def speed_controller(u, v, _dt):
        throttle = (v - u) / 50
        boost = throttle > 1.0
        return throttle, boost

    dt = 1 / 120
    seconds = 10

    sim1 = Sim()
    sim2 = Sim()
    times = [i * dt for i in range(int(seconds * (1 / dt)))]
    targets = [
        sin(time * 12) * 200 - sin(time * 8) * 300 + sin(time) * 500 for time in times
    ]
    simple_vel = []
    simple_err = []
    drive_vel = []
    drive_err = []
    for time, target in zip(times, targets):
        simple_vel.append(sim1.vel)
        drive_vel.append(sim2.vel)

        throttle, boost = speed_controller(sim1.vel, target, dt)
        sim1.step(dt, throttle, boost)
        throttle, boost = drive_speed_controller(sim2.vel, target, dt)
        sim2.step(dt, throttle, boost)

        simple_err.append(target - sim1.vel)
        drive_err.append(target - sim2.vel)

    print("[Simple] boost used:", sim1.boost_used)
    print("[Drive] boost used:", sim2.boost_used)

    print(
        "[Simple] std dev",
        sqrt(sum(map(lambda err: err * err, simple_err)) / len(simple_err)),
    )
    print(
        "[Drive] std dev",
        sqrt(sum(map(lambda err: err * err, drive_err)) / len(drive_err)),
    )

    plt.plot(times, targets)
    plt.plot(times, simple_vel)
    plt.plot(times, drive_vel)
    plt.show()

    plt.plot(times, targets)
    plt.plot(times, simple_err)
    plt.plot(times, drive_err)
    plt.plot(times, [0 for t in times])
    plt.show()
