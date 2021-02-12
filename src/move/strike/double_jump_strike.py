from typing import Callable

from utils.const import MAX_JUMP_HEIGHT as MAX_JUMP_HEIGHT_CONST
from utils.const import MAX_DOUBLE_JUMP_HEIGHT as MAX_DOUBLE_JUMP_HEIGHT_CONST
from utils.const import double_jump_height_to_time
from utils.game_info import GameInfo
from move.double_jump import DoubleJump
from rlutilities.simulation import Ball
from move.strike.jump_strike import JumpStrike
from rlutilities.linear_algebra import vec3


class DoubleJumpStrike(JumpStrike):
    MIN_JUMP_HEIGHT: float = MAX_JUMP_HEIGHT_CONST
    MAX_JUMP_HEIGHT: float = MAX_DOUBLE_JUMP_HEIGHT_CONST + 60
    JUMP_HEIGHT_TO_TIME: Callable[[float], float] = double_jump_height_to_time

    def __init__(self, info: GameInfo, target: Ball, goal: vec3):
        super().__init__(info, target, goal)

    def start_jump(self, time_left: float):
        self.jump = DoubleJump(self.info, self.target_position)
        self.jump.update()
        self.controls = self.jump.controls
        self.controls.throttle = self.drive.controls.throttle
