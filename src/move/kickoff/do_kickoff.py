from math import sin
from typing import Optional

from move.move import Move
from move.drive import Drive
from utils.game_info import GameInfo
from rlutilities.simulation import GameState
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
        # Wait until kickoff.
        if self.info.state == GameState.Inactive:
            self.controls.throttle = 1
            self.controls.steer = sin(self.info.time * 8)  # Wiggle.
            return

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
        if self.kickoff:
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
