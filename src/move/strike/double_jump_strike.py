from typing import Tuple, Callable

from utils.game_info import GameInfo
from move.double_jump import DoubleJump
from utils.jump_prediction import solve_double_jump
from rlutilities.simulation import Car, Ball
from move.strike.jump_strike import JumpStrike
from rlutilities.linear_algebra import vec3


class DoubleJumpStrike(JumpStrike):
    OFFSET_DISTANCE: float = Ball.collision_radius
    SOLVE_JUMP: Callable[[Car, vec3, vec3], Tuple[vec3, float]] = solve_double_jump

    def __init__(self, info: GameInfo, target: Ball, goal: vec3):
        super().__init__(info, target, goal)

    @staticmethod
    def get_height_min_max(info: GameInfo) -> Tuple[float, float]:
        return info.MAX_JUMP_HEIGHT, info.MAX_DOUBLE_JUMP_HEIGHT + 60

    @staticmethod
    def get_max_time_to_jump(info: GameInfo) -> float:
        return info.DOUBLE_JUMP_PEAK_TIME + 0.2

    def start_jump(self, time_left: float):
        self.jump = DoubleJump(self.info, self.target_position)
        self.jump.update()
        self.controls = self.jump.controls
        self.controls.throttle = self.drive.controls.throttle
