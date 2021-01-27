from typing import List, Optional

from rlbot.agents.base_agent import BaseAgent
from rlbot.utils.structures.game_data_struct import GameTickPacket, FieldInfoPacket
from rlbot.utils.structures.ball_prediction_struct import BallPrediction

from utils.match_settings import Map, GameMode, ParsedMatchSettings
from rlutilities.simulation import Car, Ball, Game, BoostPad, BoostPadType
from rlutilities.linear_algebra import vec3


class GameInfo(Game):
    def __init__(self, agent: BaseAgent):
        super().__init__()
        self.index = agent.index
        self.logger = agent.logger
        self.large_boost_pads: List[BoostPad] = []
        self.small_boost_pads: List[BoostPad] = []
        self.dt: float = 0.00833333333
        self.prev_time: float = 0.0
        self.settings: ParsedMatchSettings = ParsedMatchSettings(
            agent.get_match_settings()
        )
        self.setup_mode()
        self.read_field_info(agent.get_field_info())
        self.setup_ball_prediction(agent.get_ball_prediction_struct())

    def update(
        self, packet: GameTickPacket, ball_prediction: BallPrediction,
    ):
        self.read_packet(packet)
        self.update_ball_prediction(ball_prediction)

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

    def get_teammates(self, carol: Car) -> List[Car]:
        return [
            car for car in self.cars if car.team == carol.team and car.id != carol.id
        ]

    def get_opponents(self, carol: Car) -> List[Car]:
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

    def setup_ball_prediction(self, ball_prediction: BallPrediction):
        self.ball_prediction: List[Ball] = [
            Ball(self.ball) for _ in range(ball_prediction.num_slices)
        ]

    def update_ball_prediction(self, ball_prediction: BallPrediction):
        if len(self.ball_prediction) != ball_prediction.num_slices:
            self.setup_ball_prediction(ball_prediction)
        for i, frame in enumerate(ball_prediction.slices[: ball_prediction.num_slices]):
            self.ball_prediction[i].position = vec3(
                frame.physics.location.x,
                frame.physics.location.y,
                frame.physics.location.z,
            )
            self.ball_prediction[i].velocity = vec3(
                frame.physics.velocity.x,
                frame.physics.velocity.y,
                frame.physics.velocity.z,
            )
            self.ball_prediction[i].angular_velocity = vec3(
                frame.physics.angular_velocity.x,
                frame.physics.angular_velocity.y,
                frame.physics.angular_velocity.z,
            )
            self.ball_prediction[i].time = frame.game_seconds
