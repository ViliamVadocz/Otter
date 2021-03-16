from typing import Tuple, Callable

from utils.const import DEFAULT_DOUBLE_JUMP_PEAK_TIME
from utils.game_info import GameInfo
from move.double_jump import DoubleJump
from utils.jump_prediction import solve_double_jump, time_to_reach_double_jump_height
from rlutilities.simulation import Car, Ball
from move.strike.jump_strike import JumpStrike
from rlutilities.linear_algebra import vec3


class DoubleJumpStrike(JumpStrike):
    OFFSET_DISTANCE: float = Ball.collision_radius

    SOLVE_JUMP: Callable[[Car, vec3, vec3], Tuple[vec3, float]] = solve_double_jump
    JUMP_HEIGHT_TO_TIME: Callable[
        [float, float], float
    ] = time_to_reach_double_jump_height
    JUMP_PEAK_TIME: float = DEFAULT_DOUBLE_JUMP_PEAK_TIME

    def __init__(self, info: GameInfo, target: Ball, goal: vec3):
        super().__init__(info, target, goal)

    def start_jump(self, time_left: float):
        self.jump = DoubleJump(self.info, self.target_position)
        self.jump.update()
        self.controls = self.jump.controls
        self.controls.throttle = self.drive.controls.throttle
