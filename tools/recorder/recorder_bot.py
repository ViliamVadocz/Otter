# https://github.com/RLBot/RLBotPythonExample/wiki/Input-and-Output-Data#sample-game-tick-packet
# https://github.com/RLBot/RLBotPythonExample/wiki/Manipulating-Game-State

from math import pi
from typing import List, Tuple

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.game_state_util import Physics, Rotator, Vector3, CarState, GameState
from rlbot.utils.structures.game_data_struct import GameTickPacket


class Flute(BaseAgent):
    def is_hot_reload_enabled(self):
        return False

    def initialize_agent(self):
        self.controls: SimpleControllerState = SimpleControllerState()
        self.last_set_time: float = -float("inf")
        self.data: List[Tuple] = []

        self.reset_time: float = 1.8
        self.delay_time: float = 1.5

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        if not packet.game_info.is_round_active:
            return self.controls
        expired_time: float = packet.game_info.seconds_elapsed - self.last_set_time - self.delay_time
        if expired_time > self.reset_time:
            self.last_set_time = packet.game_info.seconds_elapsed
            self.set_state()
            self.controls = SimpleControllerState()
            print("\n" + str(self.data) + "\n")
            self.data.clear()
            return self.controls
        if expired_time < 0:
            return self.controls
        self.data.append(self.get_values(expired_time, packet))
        return self.get_controls(expired_time)

    def set_state(self):
        car_state: CarState = CarState(
            physics=Physics(
                location=Vector3(1000, -3000, 18),
                velocity=Vector3(0, 0, 0),
                rotation=Rotator(0, pi / 2, 0),
                angular_velocity=Vector3(0, 0, 0),
            ),
        )
        game_state: GameState = GameState(cars={self.index: car_state})
        self.set_game_state(game_state)

    def get_controls(self, time: float) -> SimpleControllerState:
        return SimpleControllerState(throttle=1, boost=True)

    def get_values(self, time: float, packet: GameTickPacket) -> Tuple[float]:
        return (
            time,
            packet.game_cars[self.index].physics.velocity.y,
            packet.game_cars[self.index].physics.location.y + 3000,
        )


if __name__ == "__main__":

    from rlbot.setup_manager import SetupManager

    manager = SetupManager()
    manager.load_config(config_location="recorder_match.cfg")
    manager.connect_to_game()
    manager.start_match()
    manager.launch_bot_processes()
