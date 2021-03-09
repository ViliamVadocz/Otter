from typing import List, Optional

from rlbot.agents.base_agent import BaseAgent
from rlbot.utils.structures.game_data_struct import GameTickPacket

from utils.const import (
    DEFAULT_JUMP_PEAK_TIME,
    DEFAULT_MAX_JUMP_HEIGHT,
    DEFAULT_DOUBLE_JUMP_PEAK_TIME,
    DEFAULT_MAX_DOUBLE_JUMP_HEIGHT,
)
from utils.arena.arena import Arena
from utils.match_settings import Map, GameMode, ParsedMatchSettings
from utils.goal_prediction import GoalPrediction
from utils.jump_prediction import get_jump_peak, get_double_jump_peak
from rlutilities.simulation import Car, Ball, Game, BoostPad, BoostPadType
from rlutilities.linear_algebra import norm, vec3
from utils.arena.standard_arena import StandardArena

BALL_PREDICT_DT = 1 / 120
BALL_PREDICT_NUM = 720


class GameInfo(Game):
    def __init__(self, agent: BaseAgent):
        super().__init__()
        self.index = agent.index
        self.logger = agent.logger
        self.dt: float = 0.00833333333
        self.prev_time: float = 0.0
        self.prev_gravity: vec3 = vec3(self.gravity)
        self.MAX_JUMP_HEIGHT: float = DEFAULT_MAX_JUMP_HEIGHT
        self.JUMP_PEAK_TIME: float = DEFAULT_JUMP_PEAK_TIME
        self.MAX_DOUBLE_JUMP_HEIGHT: float = DEFAULT_MAX_DOUBLE_JUMP_HEIGHT
        self.DOUBLE_JUMP_PEAK_TIME: float = DEFAULT_DOUBLE_JUMP_PEAK_TIME
        self.goal_prediction: Optional[GoalPrediction] = None
        self.settings: ParsedMatchSettings = ParsedMatchSettings(
            agent.get_match_settings()
        )
        self.arena: Arena = None
        self.setup_mode()
        self.read_field_info(agent.get_field_info())
        self._reset_ball_prediction()

    def update(self, packet: GameTickPacket):
        self.read_packet(packet)
        self._reset_ball_prediction()

        self.dt = self.time - self.prev_time
        self.prev_time = self.time

        if norm(self.gravity - self.prev_gravity) > 0.1:
            self.prev_gravity = vec3(self.gravity)
            self.MAX_JUMP_HEIGHT, self.JUMP_PEAK_TIME = get_jump_peak(self.gravity)
            (
                self.MAX_DOUBLE_JUMP_HEIGHT,
                self.DOUBLE_JUMP_PEAK_TIME,
            ) = get_double_jump_peak(self.gravity)

    def get_teammates(self, carol: Car = None) -> List[Car]:
        if not carol:
            carol = self.car
        return [
            car for car in self.cars if car.team == carol.team and car.id != carol.id
        ]

    def get_opponents(self, carol: Car = None) -> List[Car]:
        if not carol:
            carol = self.car
        return [car for car in self.cars if car.team != carol.team]

    @property
    def car(self) -> Car:
        return self.cars[self.index]

    def setup_mode(self):
        # TODO Custom map support?
        # if settings.map == Map.UtopiaRetro:
        if self.settings.map == Map.ThrowbackStadium:
            self.set_mode("throwback")
        elif self.settings.game_mode == GameMode.Soccer:
            self.set_mode("soccar")
        elif self.settings.game_mode == GameMode.Hoops:
            self.set_mode("hoops")
        elif self.settings.game_mode == GameMode.Dropshot:
            self.set_mode("dropshot")
        else:
            # TODO Hockey, Rumble, Heatseeker
            self.logger.warn(f"Unknown game mode: {self.settings.game_mode}")
            self.set_mode("soccar")

        self.arena = StandardArena()

    def _reset_ball_prediction(self):
        self.ball_prediction: List[Ball] = [Ball(self.ball)]
        for _ in range(BALL_PREDICT_NUM):
            ball: Ball = Ball(self.ball_prediction[-1])
            ball.step(BALL_PREDICT_DT)
            self.ball_prediction.append(ball)

    def _update_ball_prediction(self):
        if close_ball(self.ball, self.ball_prediction[1]):
            for i in range(BALL_PREDICT_NUM):
                if self.ball_prediction[i].time < self.time + 0.5 * BALL_PREDICT_DT:
                    continue
                for _ in range(i):
                    ball: Ball = Ball(self.ball_prediction[-1])
                    ball.step(BALL_PREDICT_DT)
                    self.ball_prediction.append(ball)
                    del self.ball_prediction[0]
                break
        else:
            self._reset_ball_prediction()


def close_ball(predicted: Ball, actual: Ball) -> bool:
    return (
        abs(predicted.velocity.x - actual.velocity.x)
        + abs(predicted.velocity.y - actual.velocity.y)
        + abs(predicted.velocity.z - actual.velocity.z)
        < 10.0
    )


def team_sign(team: int) -> float:
    return team * -2 + 1
