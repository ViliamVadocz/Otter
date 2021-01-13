from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket

from utils.game_info import GameInfo


class MyBot(BaseAgent):
    def initialize_agent(self):
        self.info = GameInfo(self.team)
        self.info.set_mode("soccar")
        self.ctrl = SimpleControllerState()

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        self.info.update(
            packet, self.get_field_info(), self.get_ball_prediction_struct()
        )
        self.ctrl = SimpleControllerState()
        self.renderer.draw_polyline_3d(
            [step.physics.location for step in self.info.ball_prediction.slices][::20],
            self.renderer.cyan(),
        )
        return self.ctrl
