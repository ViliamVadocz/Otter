from rlutilities.linear_algebra import dot, norm, vec3


def dist(a: vec3, b: vec3) -> float:
    return norm(a - b)


def flatten_by_normal(vec: vec3, normal: vec3) -> vec3:
    return vec - dot(vec, normal) * normal
