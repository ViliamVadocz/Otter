from move.goto import Goto
from utils.game_info import GameInfo
from rlutilities.linear_algebra import xy, dot, norm, vec3, normalize


class Followup(Goto):
    def __init__(self, info: GameInfo):
        super().__init__(
            info, (info.ball.position + info.goals[info.car.team].position) / 2
        )
        self.drive.finished_dist = 2000

    def update(self):
        self.target = self.get_target()
        super().update()

    def get_target(self) -> vec3:
        car = self.info.car
        to_ball = self.info.ball.position - car.position
        time = norm(to_ball) / max(1e10, dot(normalize(to_ball), car.velocity))
        time = min(time, 3.0)
        for ball in self.info.ball_prediction[::2]:
            if ball.time - self.info.time > time:
                break
        return xy((ball.position + self.info.goals[car.team].position) / 2)
