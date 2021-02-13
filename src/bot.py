from rlbot.agents.base_agent import BaseAgent
from rlbot.utils.structures.game_data_struct import GameTickPacket

from utils import rendering
from utils.game_info import GameInfo
from strategy.strategy import Strategy
from utils.match_settings import GameMode
from rlutilities.simulation import Game, Input
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
        self.info.update(packet)
        # Only render as the lowest index Otter
        if (
            min(
                index
                for index, car in enumerate(packet.game_cars[: packet.num_cars])
                if "Otter" in car.name
            )
            == self.index
        ):
            self.render()
        self.strategy.update()
        return self.strategy.controls

    def pick_strategy(self) -> Strategy:
        if self.info.settings.game_mode == GameMode.Soccer:
            return SoccarStrategy(self.info)
        return DefaultStrategy(self.info)

    def render(self):
        MIN_PREDICTION = 100
        PREDICTION_STEP = 50
        if len(self.info.ball_prediction) > MIN_PREDICTION:
            rendering.begin_rendering("ball prediction")
            rendering.draw_polyline_3d(
                [
                    ball.position
                    for ball in self.info.ball_prediction[::PREDICTION_STEP]
                ],
                rendering.cyan(),
            )
            rendering.end_rendering()

            rendering.begin_rendering("goal prediction")
            if self.info.goal_prediction:
                ball = self.info.goal_prediction.ball
                rendering.draw_rect_3d(
                    ball.position, 10, 10, True, rendering.white(),
                )
                rendering.draw_string_3d(
                    ball.position,
                    2,
                    2,
                    f"{ball.time - self.info.time:.2f}",
                    rendering.white(),
                )
            rendering.end_rendering()
