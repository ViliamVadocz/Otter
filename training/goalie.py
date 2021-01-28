from math import pi, sqrt
from pathlib import Path
from dataclasses import dataclass

from rlbottraining.rng import SeededRandomNumberGenerator
from rlbot.utils.game_state_util import (
    Physics,
    Rotator,
    Vector3,
    CarState,
    BallState,
    GameState,
)
from rlbot.matchconfig.match_config import Team, PlayerConfig
from rlbottraining.training_exercise import Playlist
from rlbottraining.common_exercises.common_base_exercises import GoalieExercise


class vec3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"vec3({self.x}, {self.y}, {self.z})"

    def __add__(self, other: "vec3") -> "vec3":
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "vec3") -> "vec3":
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, k: float) -> "vec3":
        return vec3(self.x * k, self.y * k, self.z * k)

    def __rmul__(self, k: float) -> "vec3":
        return self.__mul__(k)

    def __truediv__(self, k: float) -> "vec3":
        return vec3(self.x / k, self.y / k, self.z / k)

    def norm(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def unit(self) -> "vec3":
        return self / self.norm()

    def done(self) -> Vector3:
        return Vector3(self.x, self.y, self.z)


@dataclass
class RollingBall(GoalieExercise):
    def make_game_state(self, rng: SeededRandomNumberGenerator) -> GameState:
        ball_pos = vec3(rng.uniform(-2000, 2000), 0, 100)
        target = vec3(rng.uniform(-700, 700), -5200, 100)
        vel_dir = (target - ball_pos).unit()

        ball = BallState(
            physics=Physics(
                location=ball_pos.done(),
                velocity=(vel_dir * rng.uniform(1500, 2000)).done(),
            )
        )

        car = CarState(
            physics=Physics(
                location=Vector3(rng.uniform(-2000, 2000), -4000, 20),
                rotation=Rotator(0, pi / 2, 0),
            )
        )

        return GameState(ball=ball, cars={0: car})


def make_default_playlist() -> Playlist:
    exercises = [RollingBall("RollingBall")]
    config = [
        PlayerConfig.bot_config(
            Path(__file__).absolute().parent.parent / "src" / "bot.cfg", Team.BLUE
        )
    ]
    for ex in exercises:
        ex.match_config.player_configs = config
    return exercises


if __name__ == "__main__":
    from rlbottraining.exercise_runner import run_module

    run_module(Path(__file__))
