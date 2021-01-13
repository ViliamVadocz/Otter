from rlutilities.mechanics import Drive
from utils.game_info import GameInfo
from move.move import Move


class ChaseBall(Move):
    def __init__(self, info: GameInfo):
        super().__init__(info)
        self.drive = Drive(info.car)

    def update(self):
        self.drive.target = self.info.ball.position
        self.drive.step(self.info.time_delta)
        self.controls = self.drive.controls
