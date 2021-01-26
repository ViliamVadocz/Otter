from typing import List, Optional

from rlbot.agents.base_agent import BaseAgent
from rlbot.utils.structures.game_data_struct import GameTickPacket, FieldInfoPacket
from rlbot.utils.structures.ball_prediction_struct import BallPrediction

from utils.match_settings import Map, GameMode, ParsedMatchSettings
from rlutilities.simulation import Car, Pad, Ball, Game


class GameInfo(Game):
    def __init__(self, agent: BaseAgent):
        super().__init__(agent.index, agent.team)
        self.logger = agent.logger
        self.ball_prediction: BallPrediction = []
        self.large_boost_pads: List[Pad] = []
        self.small_boost_pads: List[Pad] = []
        self.settings: ParsedMatchSettings = ParsedMatchSettings(
            agent.get_match_settings()
        )
        self.setup_mode()

    def update(
        self,
        packet: GameTickPacket,
        field_info: FieldInfoPacket,
        ball_prediction: BallPrediction,
    ):
        self.read_game_information(packet, field_info)
        self.ball_prediction = (
            ball_prediction  # TODO Maybe convert to RLU Ball objects.
        )
        self.large_boost_pads = [
            self.pads[i]
            for i in range(field_info.num_boosts)
            if field_info.boost_pads[i].is_full_boost
        ]
        self.small_boost_pads = [
            self.pads[i]
            for i in range(field_info.num_boosts)
            if not field_info.boost_pads[i].is_full_boost
        ]

        # Invert boost pad timers.
        for pad in self.large_boost_pads:
            pad.timer = 10.0 - pad.timer
        for pad in self.small_boost_pads:
            pad.timer = 4.0 - pad.timer

    def get_teammates(self, car: Car) -> List[Car]:
        return [
            self.cars[i]
            for i in range(self.num_cars)
            if self.cars[i].team == self.team and self.cars[i].id != car.id
        ]

    def get_opponents(self, car: Car) -> List[Car]:
        return [
            self.cars[i] for i in range(self.num_cars) if self.cars[i].team != car.team
        ]

    @property
    def index(self):
        return self.id

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
