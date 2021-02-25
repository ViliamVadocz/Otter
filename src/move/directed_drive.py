from move.drive import DEFAULT_FINISHED_DIST, Drive
from utils.vectors import dist, flatten_by_normal
from utils.game_info import GameInfo
from rlutilities.linear_algebra import vec3, normalize

DEFAULT_DIST_FRACTION = 1 / 3


class DirectedDrive(Drive):
    def __init__(
        self,
        info: GameInfo,
        target: vec3,
        direction: vec3,
        finished_dist: float = DEFAULT_FINISHED_DIST,
        DIST_FRACTION=DEFAULT_DIST_FRACTION,
    ):
        super().__init__(info, target, finished_dist=finished_dist)
        self.dist_fraction = DEFAULT_DIST_FRACTION
        self.final_target = target
        self.direction = direction

    def update(self):
        car = self.info.car
        distance = dist(self.final_target, car.position)
        self.target = (
            self.final_target
            - normalize(flatten_by_normal(self.direction, car.up()))
            * self.dist_fraction
            * distance
        )

        super().update()
