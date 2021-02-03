from math import pi, acos, atan2
from typing import Tuple

from rlutilities.linear_algebra import norm, vec2


class Circle:
    def __init__(self, centre: vec2, radius: float):
        self.centre: vec2 = centre
        self.radius: float = radius


# https://stackoverflow.com/a/2323034
def normalize180(angle: float) -> float:
    angle = ((angle % (pi * 2)) + pi * 2) % (pi * 2)
    if angle > pi:
        angle -= pi * 2
    return angle


# https://stackoverflow.com/a/49987361
def get_tangent_angles(point: vec2, circle: Circle) -> Tuple[float, float]:
    th = acos(min(1, circle.radius / norm(point - circle.centre)))
    d = atan2(point.y - circle.centre.y, point.x - circle.centre.x)
    return d - th, d + th


# https://stackoverflow.com/a/42248572
def clamp_angle(angle: float, min: float, max: float) -> float:
    n_min: float = normalize180(min - angle)
    n_max: float = normalize180(max - angle)

    if n_min <= 0 <= n_max:
        return angle
    if abs(n_min) < abs(n_max):
        return min
    return max


if __name__ == "__main__":
    from math import degrees, radians

    circle: Circle = Circle(vec2(10, 10), radius=2)
    point: vec2 = vec2(-20, 10)
    tangent_angles: Tuple[float, float] = get_tangent_angles(point, circle)
    print([degrees(angle) for angle in tangent_angles])
    while True:
        angle: float = radians(float(input("Angle: ")))
        print(degrees(clamp_angle(angle, *tangent_angles)))
        print()
