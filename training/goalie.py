from math import pi, acos
from pathlib import Path
from dataclasses import dataclass

from vec import vec3
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
                location=Vector3(rng.uniform(-2000, 2000), -4000, 0),
                velocity=Vector3(0, 0, 0),
                rotation=Rotator(0, pi / 2, 0),
                angular_velocity=Vector3(0, 0, 0),
            ),
            boost_amount=40,
        )

        return GameState(ball=ball, cars={0: car})


@dataclass
class BouncingBall(GoalieExercise):
    def make_game_state(self, rng: SeededRandomNumberGenerator) -> GameState:
        ball_pos = vec3(rng.uniform(-2000, 2000), 0, 1000)
        target = vec3(rng.uniform(-700, 700), -5200, 100)
        vel_dir = (target - ball_pos - vec3(0, 0, 800)).unit()

        ball = BallState(
            physics=Physics(
                location=ball_pos.done(),
                velocity=(vel_dir * rng.uniform(1700, 2300)).done(),
            )
        )

        car = CarState(
            physics=Physics(
                location=Vector3(rng.uniform(-2000, 2000), -3000, 0),
                velocity=Vector3(0, 0, 0),
                rotation=Rotator(0, pi / 2, 0),
                angular_velocity=Vector3(0, 0, 0),
            ),
            boost_amount=40,
        )

        return GameState(ball=ball, cars={0: car})


def make_default_playlist() -> Playlist:
    exercises = [RollingBall("RollingBall"), BouncingBall("BouncingBall")]
    config = [
        PlayerConfig.bot_config(
            Path(__file__).absolute().parent.parent / "src" / "bot.cfg", Team.BLUE
        )
    ]
    for i, player in enumerate(config):
        player.spawn_id = i + 1
    for ex in exercises:
        ex.match_config.player_configs = config
    return exercises


if __name__ == "__main__":
    from rlbottraining.exercise_runner import run_module

    run_module(Path(__file__))
