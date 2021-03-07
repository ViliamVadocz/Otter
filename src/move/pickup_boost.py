from move.goto import Goto
from utils.game_info import GameInfo
from rlutilities.simulation import BoostPad, BoostPadType, BoostPadState


class PickupBoost(Goto):
    def __init__(self, info: GameInfo, pad: BoostPad):
        super().__init__(info, pad.position)
        self.pad: BoostPad = pad

    def update(self):
        super().update()
        if self.pad.type == BoostPadType.Partial:
            self.controls.boost = False
        self.finished = (
            self.info.car.boost > 99 or self.pad.state == BoostPadState.Unavailable
        )
