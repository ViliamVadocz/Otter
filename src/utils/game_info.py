from typing import List, Optional

from rlbot.agents.base_agent import BaseAgent
from rlbot.utils.structures.game_data_struct import GameTickPacket, FieldInfoPacket
from rlbot.utils.structures.ball_prediction_struct import BallPrediction

from utils.match_settings import Map, GameMode, ParsedMatchSettings
from rlutilities.simulation import Car, Ball, Game, BoostPad, BoostPadType


class GameInfo(Game):
    def __init__(self, agent: BaseAgent):
        super().__init__()
        self.index = agent.index
        self.logger = agent.logger
        self.ball_prediction: BallPrediction = []
        self.large_boost_pads: List[BoostPad] = []
        self.small_boost_pads: List[BoostPad] = []
        self.dt: float = 0.00833333333
        self.prev_time: float = 0.0
        self.settings: ParsedMatchSettings = ParsedMatchSettings(
            agent.get_match_settings()
        )
        self.setup_mode()
        self.read_field_info(agent.get_field_info())

    def update(
        self, packet: GameTickPacket, ball_prediction: BallPrediction,
    ):
        self.read_packet(packet)
        self.ball_prediction = (
            ball_prediction  # TODO Maybe convert to RLU Ball objects.
        )
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
        # TODO Hockey, Rumble, Heatseeker
        else:
            self.logger.warn(f"Unknown game mode: {self.settings.game_mode}")
            self.set_mode("soccar")
