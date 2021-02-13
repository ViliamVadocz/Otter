from rlutilities.linear_algebra import dot, norm, vec3, normalize


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
