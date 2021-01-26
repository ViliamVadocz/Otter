from rlbot.agents.base_agent import BaseAgent
from rlbot.utils.structures.game_data_struct import GameTickPacket, FieldInfoPacket

from utils.game_info import GameInfo
from strategy.strategy import Strategy
from utils.match_settings import GameMode
from rlutilities.simulation import Input
from strategy.soccar_strategy import SoccarStrategy
from strategy.default_strategy import DefaultStrategy


class Otter(BaseAgent):
    def is_hot_reload_enabled(self):
        return False

    def initialize_agent(self):
        self.info: GameInfo = GameInfo(self)
        self.strategy: Strategy = self.pick_strategy()
        self.field_info: FieldInfoPacket = self.get_field_info()

    def get_output(self, packet: GameTickPacket) -> Input:
        self.info.update(packet, self.field_info, self.get_ball_prediction_struct())

        self.renderer.begin_rendering("path prediction")
        self.renderer.draw_polyline_3d(
            [step.physics.location for step in self.info.ball_prediction.slices][::20],
            self.renderer.cyan(),
        )
        self.renderer.end_rendering()

        self.strategy.update()
        return self.strategy.controls

    def pick_strategy(self) -> Strategy:
        if self.info.settings.game_mode == GameMode.Soccer:
            return SoccarStrategy(self.info, self.renderer)
        return DefaultStrategy(self.info, self.renderer)
