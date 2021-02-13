from typing import List, Optional

from rlbot.agents.base_agent import BaseAgent
from rlbot.utils.structures.game_data_struct import GameTickPacket

from utils.match_settings import Map, GameMode, ParsedMatchSettings
from utils.goal_prediction import GoalPrediction
from rlutilities.simulation import Car, Ball, Game, BoostPad, BoostPadType

BALL_PREDICT_DT = 1 / 120
BALL_PREDICT_NUM = 720


class GameInfo(Game):
    def __init__(self, agent: BaseAgent):
        super().__init__()
        self.index = agent.index
        self.logger = agent.logger
        self.large_boost_pads: List[BoostPad] = []
        self.small_boost_pads: List[BoostPad] = []
        self.dt: float = 0.00833333333
        self.prev_time: float = 0.0
        self.goal_prediction: Optional[GoalPrediction] = None
        self.settings: ParsedMatchSettings = ParsedMatchSettings(
            agent.get_match_settings()
        )
        self.setup_mode()
        self.read_field_info(agent.get_field_info())
        self.reset_ball_prediction()

    def update(self, packet: GameTickPacket):
        self.read_packet(packet)
        if self.frame == 0:
            print("hi")
        self.reset_ball_prediction()
        # Sort of expensive and it is not needed yet.
        # self.goal_prediction = get_goal_prediction(self.ball_prediction, self.goals)

        self.large_pads = [pad for pad in self.pads if pad.type == BoostPadType.Full]
        self.small_pads = [pad for pad in self.pads if pad.type == BoostPadType.Partial]

        # Invert boost pad timers.
        # TODO Verify that this didn't change. If it did, remove.
        for pad in self.large_boost_pads:
            pad.timer = 10.0 - pad.timer
        for pad in self.small_boost_pads:
            pad.timer = 4.0 - pad.timer

        self.dt = self.time - self.prev_time
        self.prev_time = self.time

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
    def car(self):
        return self.cars[self.index]

    def setup_mode(self):
        import rlutilities

        # TODO Custom map support?
        # if settings.map == Map.UtopiaRetro:
        if self.settings.map == Map.ThrowbackStadium:
            rlutilities.initialize("throwback")
        elif self.settings.game_mode == GameMode.Soccer:
            rlutilities.initialize("soccar")
        elif self.settings.game_mode == GameMode.Hoops:
            rlutilities.initialize("hoops")
        elif self.settings.game_mode == GameMode.Dropshot:
            rlutilities.initialize("dropshot")
        # TODO Hockey, Rumble, Heatseeker
        else:
            self.logger.warn(f"Unknown game mode: {self.settings.game_mode}")
            rlutilities.initialize("soccar")

    def reset_ball_prediction(self):
        self.ball_prediction: List[Ball] = []
        ball = Ball(self.ball)
        for _ in range(BALL_PREDICT_NUM):
            self.ball_prediction.append(ball)
            ball = Ball(ball)
            ball.step(BALL_PREDICT_DT)

    def update_ball_prediction(self):
        if close_ball(self.ball, self.ball_prediction[1]):
            self.ball_prediction[:-1] = self.ball_prediction[1:]
            self.ball_prediction[-1].step(BALL_PREDICT_DT)
        else:
            self.setup_ball_prediction()


def close_ball(predicted: Ball, actual: Ball) -> bool:
    return (
        abs(predicted.velocity.x - actual.velocity.x)
        + abs(predicted.velocity.y - actual.velocity.y)
        + abs(predicted.velocity.z - actual.velocity.z)
        < 10.0
    )
