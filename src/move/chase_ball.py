from move.move import Move
from utils.game_info import GameInfo
from rlutilities.mechanics import Drive
from rlutilities.simulation import Car
from rlutilities.linear_algebra import dot, norm, vec3, normalize


class ChaseBall(Move):
    def __init__(self, info: GameInfo):
        super().__init__(info)
        self.drive = Drive(info.car)

    def update(self):
        car: Car = self.info.car
        if (
            norm(car.velocity) + car.boost / 33.3 * 1060 < 2200
            and not self.info.kickoff_pause
        ):
            self.drive.target = min(
                self.info.large_boost_pads,
                key=lambda b: norm(b.position - car.position)
                + (0 if b.is_active else 1e10),
            ).position
        else:
            self.drive.target = self.info.ball.position
            goal: vec3 = vec3(
                max(-600, min(600, self.info.ball.position[0])),
                5120 * (car.team * -2 + 1),
                0,
            )
            self.drive.target += max(
                100, norm(self.info.ball.position - car.position) * 0.2
            ) * normalize(self.info.ball.position - goal)

        local_target: vec3 = dot(car.orientation, self.drive.target - car.position)
        radius: float = (local_target[0] ** 2 + local_target[1] ** 2) / (
            2 * max(1, abs(local_target[1]) - 130)
        )
        self.drive.speed = get_speed_from_radius(radius)

        self.drive.step(self.info.dt)
        self.controls = self.drive.controls
        self.controls.boost &= not car.supersonic and car.on_ground


def get_speed_from_radius(radius: float) -> float:
    curvature: float = 1 / max(1 ** -10, abs(radius))
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
