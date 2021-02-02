from move.goto import Goto
from utils.game_info import GameInfo
from rlutilities.simulation import BoostPad, BoostPadState


class PickupBoost(Goto):
    def __init__(self, info: GameInfo, pad: BoostPad):
        super().__init__(info, pad.position)
        self.pad: BoostPad = pad

    def update(self):
        super().update()
        self.finished = (
            self.info.car.boost > 99 or self.pad.state == BoostPadState.Unavailable
        )
