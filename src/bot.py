from rlbot.utils.structures.game_data_struct import GameTickPacket
from rlbot.agents.base_agent import BaseAgent

from strategy.soccar_strategy import SoccarStrategy
from rlutilities.simulation import Input
from utils.game_info import GameInfo
from strategy.strategy import Strategy


class MyBot(BaseAgent):
    def initialize_agent(self):
        self.info = GameInfo(self.index, self.team, self.renderer)
        self.info.set_mode("soccar")
        self.field_info = self.get_field_info()
        self.strategy: Strategy = SoccarStrategy(self.info)

    def get_output(self, packet: GameTickPacket) -> Input:
        self.info.update(packet, self.field_info, self.get_ball_prediction_struct())

        self.renderer.draw_polyline_3d(
            [step.physics.location for step in self.info.ball_prediction.slices][::20],
            self.renderer.cyan(),
        )

        self.strategy.update()
        return self.strategy.move.controls
