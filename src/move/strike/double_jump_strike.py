from typing import Tuple, Callable

from utils.const import MAX_JUMP_HEIGHT as MAX_JUMP_HEIGHT_CONST
from utils.const import MAX_DOUBLE_JUMP_HEIGHT as MAX_DOUBLE_JUMP_HEIGHT_CONST
from utils.game_info import GameInfo
from move.double_jump import DoubleJump
from utils.jump_prediction import solve_double_jump
from rlutilities.simulation import Car, Ball
from move.strike.jump_strike import JumpStrike
from rlutilities.linear_algebra import vec3


class DoubleJumpStrike(JumpStrike):
    OFFSET_DISTANCE: float = Ball.collision_radius
    MIN_JUMP_HEIGHT: float = MAX_JUMP_HEIGHT_CONST
    MAX_JUMP_HEIGHT: float = MAX_DOUBLE_JUMP_HEIGHT_CONST + 60
    SOLVE_JUMP: Callable[[Car, vec3, vec3], Tuple[vec3, float]] = solve_double_jump

    def __init__(self, info: GameInfo, target: Ball, goal: vec3):
        super().__init__(info, target, goal)

    def start_jump(self, time_left: float):
        self.jump = DoubleJump(self.info, self.target_position)
        self.jump.update()
        self.controls = self.jump.controls
        self.controls.throttle = self.drive.controls.throttle
