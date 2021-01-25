from const import (
    BOOST_ACC,
    BREAK_ACC,
    COAST_ACC,
    MAX_CAR_SPEED,
    MIN_BOOST_TIME,
    throttle_acc_from_speed,
)


class Sim:
    def __init__(self):
        self.vel = 0.0
        self.boosting = False
        self.boost_time = 0.0

    def step(self, dt, throttle, boost):
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


if __name__ == "__main__":
    from math import sin

    import matplotlib.pyplot as plt

    # Replace with your own speed controller!
    def speed_controller(u, v, _dt):
        return (1.0, True) if v > u else (-1.0, False)

    sim = Sim()
    dt = 1 / 120
    seconds = 6
    t = [i * dt for i in range(int(seconds * (1 / dt)))]
    a = []
    b = []
    for time in t:
        target = sin(time) * 2000
        a.append(target)
        b.append(sim.vel)
        throttle, boost = speed_controller(sim.vel, target, dt)
        sim.step(dt, throttle, boost)
    plt.plot(t, a)
    plt.plot(t, b)
    plt.show()
