from abc import abstractmethod
from typing import List, Optional

from utils import rendering
from move.move import Move
from utils.vectors import dist
from utils.game_info import GameInfo
from rlutilities.simulation import Car, Ball
from rlutilities.linear_algebra import vec3

BALL_CHANGED_DIST = 80


class Strike(Move):
    def __init__(self, info: GameInfo, target: Ball):
        super().__init__(info)
        self.target: Ball = Ball(target)
        self.interruptible: bool = False

    def update(self):
        for ball in self.info.ball_prediction:
            if ball.time > self.target.time:
                rendering.draw_polyline_3d(
                    [
                        self.info.car.position,
                        ball.position,
                        self.target.position,
                        self.info.car.position,
                    ],
                    rendering.green(),
                )
                self.finished = (
                    dist(ball.position, self.target.position) > BALL_CHANGED_DIST
                )
                return
        self.finished = True

    @classmethod
    @abstractmethod
    def valid_target(cls, info: GameInfo, car: Car, target: vec3, time: float) -> bool:
        pass

    @classmethod
    def get_target(
        cls, info: GameInfo, car: Car = None, step: int = 1,
    ) -> Optional[Ball]:
        if not car:
            car = info.car
        return next(
            (
                ball
                for ball in info.ball_prediction[::step]
                if cls.valid_target(info, car, ball.position, ball.time)
            ),
            None,
        )
