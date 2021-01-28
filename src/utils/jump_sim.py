from const import (
    JUMP_ACC,
    JUMP_IMPULSE,
    MAX_JUMP_DURATION,
    MAX_FIRST_JUMP_HOLD,
    jump_height_to_time,
)


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


if __name__ == "__main__":
    from math import sin

    import matplotlib.pyplot as plt

    sim = Sim()
    dt = 1 / 120
    t = [i * dt for i in range(int(3 * (1 / dt)))]
    p = []
    for time in t:
        p.append(sim.pos)
        jump = (
            time < MAX_FIRST_JUMP_HOLD
            or MAX_JUMP_DURATION > time > MAX_FIRST_JUMP_HOLD + 2 * dt
        )
        sim.step(dt, jump)
    # plt.plot(t, p)  # time - height
    plt.plot(p, t)  # height - time
    plt.plot(p, [jump_height_to_time(i) for i in p])

    plt.show()
