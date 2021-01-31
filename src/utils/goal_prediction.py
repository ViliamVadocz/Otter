from typing import List, Optional

from utils import rendering
from rlutilities.simulation import Ball, Goal
from rlutilities.linear_algebra import dot, vec3, cross, normalize

GOAL_DETECTION_STEP = 20
GOAL_DEPTH = 1000


class GoalPrediction:
    def __init__(self, goal: Goal, ball: Ball):
        self.goal = goal
        self.ball = ball


# TODO Apparently goals can be any volume.
# We do not get enough info from the field_info struct
# to fully reconstruct the goals, so I am making some
# assumptions about shape and orientation.


def render_goals(goals: List[Goal], down: vec3 = vec3(0, 0, -1)):
    rendering.begin_rendering("goals")
    for goal in goals:
        width_dir = normalize(cross(down, goal.direction))
        height_dir = normalize(cross(width_dir, goal.direction))
        rendering.draw_rect_3d(
            goal.position + goal.width * width_dir / 2, 20, 20, True, rendering.green()
        )
        rendering.draw_rect_3d(
            goal.position - goal.width * width_dir / 2, 20, 20, True, rendering.green()
        )
        rendering.draw_rect_3d(
            goal.position + goal.height * height_dir / 2, 20, 20, True, rendering.blue()
        )
        rendering.draw_rect_3d(
            goal.position - goal.height * height_dir / 2, 20, 20, True, rendering.blue()
        )
        rendering.draw_rect_3d(goal.position, 20, 20, True, rendering.red())
        rendering.draw_rect_3d(
            goal.position - goal.direction * GOAL_DEPTH, 20, 20, True, rendering.white()
        )
    rendering.end_rendering()


def get_goal_prediction(
    ball_prediction: List[Ball], goals: List[Goal], down: vec3 = vec3(0, 0, -1)
) -> Optional[GoalPrediction]:
    for step, ball in enumerate(
        ball_prediction[GOAL_DETECTION_STEP::GOAL_DETECTION_STEP]
    ):
        for goal in goals:
            width_dir = normalize(cross(down, goal.direction))
            height_dir = normalize(cross(width_dir, goal.direction))

            def inside(relative_ball: vec3) -> bool:
                return (
                    abs(dot(relative_ball, width_dir)) < goal.width / 2
                    and abs(dot(relative_ball, height_dir)) < goal.height / 2
                    and -GOAL_DEPTH < dot(relative_ball, goal.direction) < 0.0
                )

            if inside(ball.position - goal.position):
                # Finer search to get the exact ball step.
                start = step * GOAL_DETECTION_STEP
                for ball in ball_prediction[start : start + GOAL_DETECTION_STEP]:
                    if inside(ball.position - goal.position):
                        return GoalPrediction(goal, ball)
    else:
        return None
