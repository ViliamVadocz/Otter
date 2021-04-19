from typing import List, Optional

from move.move import Move
from move.drive import Drive
from utils.vectors import dist
from utils.game_info import GameInfo
from rlutilities.simulation import Car, GameState
from rlutilities.linear_algebra import sgn, vec3
from move.kickoff.corner_kickoff import CornerKickoff
from move.kickoff.straight_kickoff import StraightKickoff
from move.kickoff.offcentre_kickoff import OffCentreKickoff


class DoKickoff(Move):
    def __init__(self, info: GameInfo):
        super().__init__(info)
        self.kickoff: Optional = None
        self.interruptible: bool = False
        self.dir: float = 1
        self.drive: Drive = Drive(info, vec3(0, 0, 0), 0)

    def update(self):
        # Choose kickoff.
        if not self.kickoff:
            car_position = self.info.car.position
            self.dir = -sgn(car_position.x * car_position.y)
            if abs(car_position.x) < 50:
                self.kickoff = StraightKickoff()
                self.kickoff.timer = 0.77677321434021 - 1 / 120
            elif abs(car_position.x) < 1000:
                self.kickoff = OffCentreKickoff()
                self.kickoff.timer = 0.7181718349456787 - 1 / 120
                self.dir *= -1
            else:
                self.kickoff = CornerKickoff()
                self.kickoff.timer = 0.9878482818603516 - 1 / 120

        # Execute kickoff.
        if self.kickoff.finished:
            self.drive.update()
            self.controls = self.drive.controls
        else:
            self.kickoff.step(self.info.dt)
            self.controls = self.kickoff.controls
            self.controls.roll *= self.dir
            self.controls.yaw *= self.dir
            self.controls.steer *= self.dir
        self.finished = self.info.state == GameState.Active

    @staticmethod
    def my_kickoff(info: GameInfo):
        """
        Looks for closer teammates to the ball than us,
        prioritising lower indexes.
        :param info: game info
        :return: Whether there is a closer teammate.
        """

        def distance(car: Car) -> float:
            return dist(car.position, info.ball.position) + sgn(
                car.position.x * car.position.y
            )

        our_distance: float = distance(info.car)
        closer: List[bool] = [
            distance(car) < our_distance for car in info.get_teammates()
        ]
        return not any(closer)
