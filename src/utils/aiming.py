from math import cos, sin, atan2
from typing import Tuple

from utils.angles import Circle, clamp_angle, get_tangent_angles
from rlutilities.simulation import Ball
from rlutilities.linear_algebra import xy, norm, vec2, normalize


def clamp_offset_direction(
    car_position: vec2, ball_position: vec2, ball_radius: float, offset: vec2
) -> vec2:
    circle: Circle = Circle(ball_position, ball_radius)
    tangent_angles: Tuple[float, float] = get_tangent_angles(car_position, circle)
    angle: float = atan2(offset.y, offset.x)
    angle = clamp_angle(angle, *tangent_angles)
    return vec2(cos(angle), sin(angle))


def get_offset_direction(car_position: vec2, ball: Ball, goal_position: vec2) -> vec2:
    desired_speed: float = norm(xy(ball.velocity)) + 2000  # Estimate.
    desired_velocity: vec2 = normalize(
        goal_position - xy(ball.position)
    ) * desired_speed
    desired_impulse: vec2 = desired_velocity - xy(ball.velocity)
    return clamp_offset_direction(
        car_position,
        xy(ball.position),
        ball.collision_radius,
        normalize(desired_impulse) * -1,
    )
