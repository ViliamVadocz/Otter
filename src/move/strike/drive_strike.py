from utils import rendering
from move.drive import Drive
from utils.game_info import GameInfo
from move.strike.strike import Strike
from rlutilities.simulation import Ball
from rlutilities.linear_algebra import xy, norm, vec2, vec3, normalize

OFFSET_DISTANCE: float = 115


class DriveStrike(Strike):
    def __init__(self, info: GameInfo, target: Ball, goal: vec2):
        super().__init__(info, target)
        self.target_position: vec3 = vec3(self.target.position)
        self.target_position += (
            normalize(xy(self.target_position - goal)) * OFFSET_DISTANCE
        )
        self.drive: Drive = Drive(info, self.target_position)

    def update(self):
        super().update()
        self.interruptible = not self.info.car.on_ground

        # Speed calculations.
        distance: float = norm(self.info.car.position - self.target_position)
        distance -= self.info.car.hitbox_widths.x + self.info.car.hitbox_offset.x
        self.drive.target_speed = distance / max(
            1e-10, self.target.time - self.info.time
        )

        self.drive.update()
        self.controls = self.drive.controls

        rendering.draw_line_3d(
            self.info.car.position, self.target.position, rendering.green()
        )
        rendering.draw_rect_3d(self.target.position, 2, 2, True, rendering.green())
