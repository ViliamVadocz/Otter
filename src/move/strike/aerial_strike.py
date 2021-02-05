from typing import Callable

from move.aerial import Aerial
from utils.const import MAX_JUMP_HEIGHT as MAX_JUMP_HEIGHT_CONST
from utils.const import MAX_DOUBLE_JUMP_HEIGHT as MAX_DOUBLE_JUMP_HEIGHT_CONST
from utils.const import aerial_height_to_time
from utils.game_info import GameInfo
from rlutilities.simulation import Car, Ball
from move.strike.drive_strike import DriveStrike
from rlutilities.linear_algebra import vec3

MIN_BOOST = 70

# TODO Redo this because it doesn't really work, it refuses to jump a lot


class AerialStrike(DriveStrike):
    MIN_JUMP_HEIGHT: float = MAX_DOUBLE_JUMP_HEIGHT_CONST
    MAX_JUMP_HEIGHT: float = 1800
    JUMP_HEIGHT_TO_TIME: Callable[[float], float] = aerial_height_to_time

    def __init__(self, info: GameInfo, target: Ball, goal: vec3):
        super().__init__(info, target, goal)

    def start_jump(self, time_left: float):
        self.jump = Aerial(self.info, self.target_position, self.target.time)
        self.jump.update()
        self.controls = self.jump.controls
        self.controls.throttle = self.drive.controls.throttle

    @classmethod
    def valid_target(cls, car: Car, target: vec3, time: float) -> bool:
        if car.boost < MIN_BOOST:
            return False
        return super().valid_target(car, target, time)
