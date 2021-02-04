from abc import abstractmethod

from move.move import Move
from utils.game_info import GameInfo
from rlutilities.simulation import Car, Ball
from rlutilities.linear_algebra import norm, vec3


class Strike(Move):
    def __init__(self, info: GameInfo, target: Ball):
        super().__init__(info)
        self.target: Ball = Ball(target)
        self.interruptible: bool = False

    def update(self):
        for ball in self.info.ball_prediction:
            if ball.time > self.target.time:
                self.finished = norm(ball.position - self.target.position) > 40
                return
        self.finished = True

    @classmethod
    @abstractmethod
    def valid_target(cls, car: Car, target: vec3, time: float) -> bool:
        pass
