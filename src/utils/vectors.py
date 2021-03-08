from typing import Union

from rlutilities.linear_algebra import dot, mat3, norm, vec2, vec3, cross, normalize


def dist(a: vec3, b: vec3) -> float:
    return norm(a - b)


def flatten_by_normal(vec: vec3, normal: vec3) -> vec3:
    return vec - dot(vec, normal) * normal


def direction(start: vec3, end: vec3) -> vec3:
    return normalize(end - start)


def flat_direction(start: vec3, end: vec3, normal: vec3) -> vec3:
    return normalize(flatten_by_normal(end - start, normal))


def alignment(start: vec3, middle: vec3, end: vec3, normal: vec3) -> float:
    return dot(
        flat_direction(start, middle, normal), flat_direction(middle, end, normal)
    )


def up_at(up: vec3, forward: vec3) -> mat3:
    up = normalize(up)
    left = normalize(cross(up, forward))
    forward = normalize(cross(left, up))

    # fmt: off
    return mat3(
        forward[0], left[0], up[0],
        forward[1], left[1], up[1],
        forward[2], left[2], up[2],
    )
    # fmt: on


def between(
    a: Union[vec2, vec3], point: Union[vec2, vec3], b: Union[vec2, vec3]
) -> float:
    return dot(direction(a, point), direction(point, b),)
