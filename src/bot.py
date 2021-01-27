from rlbot.agents.base_agent import BaseAgent
from rlbot.utils.structures.game_data_struct import GameTickPacket, FieldInfoPacket

from utils import rendering
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
        rendering.bind_renderer(self.renderer)

    def get_output(self, packet: GameTickPacket) -> Input:
        self.info.update(packet, self.get_ball_prediction_struct())

        rendering.begin_rendering()
        rendering.draw_polyline_3d(
            [step.physics.location for step in self.info.ball_prediction.slices][::20],
            rendering.cyan(),
        )
        self.strategy.update()
        rendering.end_rendering()
        return self.strategy.controls

    def pick_strategy(self) -> Strategy:
        if self.info.settings.game_mode == GameMode.Soccer:
            return SoccarStrategy(self.info)
        return DefaultStrategy(self.info)
