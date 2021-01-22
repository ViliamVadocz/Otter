from rlbot.agents.base_agent import BaseAgent
from rlbot.utils.structures.game_data_struct import GameTickPacket

from utils.game_info import GameInfo
from strategy.strategy import Strategy
from utils.match_settings import Map, GameMode, ParsedMatchSettings
from rlutilities.simulation import Input
from strategy.soccar_strategy import SoccarStrategy
from strategy.default_strategy import DefaultStrategy


class Otter(BaseAgent):
    def is_hot_reload_enabled(self):
        return False

    def initialize_agent(self):
        self.info = GameInfo(self.index, self.team, self.renderer)
        self.strategy: Strategy
        self.field_info = self.get_field_info()

        settings = ParsedMatchSettings(self.get_match_settings())
        # TODO Custom map support?
        # if settings.map == Map.UtopiaRetro:

        if settings.map == Map.ThrowbackStadium:
            self.info.set_mode("throwback")
            self.strategy = DefaultStrategy(self.info)

        elif settings.game_mode == GameMode.Soccer:
            self.info.set_mode("soccar")
            self.strategy = SoccarStrategy(self.info)

        elif settings.game_mode == GameMode.Hoops:
            self.info.set_mode("hoops")
            self.strategy = DefaultStrategy(self.info)

        elif settings.game_mode == GameMode.Dropshot:
            self.info.set_mode("dropshot")
            self.strategy = DefaultStrategy(self.info)

        # TODO Hokey, Rumble, Heatseeker

        else:
            self.logger.warn(f"Unknown game mode: {settings.game_mode}")
            self.info.set_mode("soccar")
            self.strategy = DefaultStrategy(self.info)

    def get_output(self, packet: GameTickPacket) -> Input:
        self.info.update(packet, self.field_info, self.get_ball_prediction_struct())

        self.renderer.draw_polyline_3d(
            [step.physics.location for step in self.info.ball_prediction.slices][::20],
            self.renderer.cyan(),
        )

        self.strategy.update()
        return self.strategy.controls
