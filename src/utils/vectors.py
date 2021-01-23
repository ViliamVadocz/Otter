from rlutilities.linear_algebra import dot, norm, vec3


def dist(a: vec3, b: vec3):
    return norm(a - b)


def flatten_by_normal(vec: vec3, normal: vec3):
    return vec - dot(vec, normal) * normal


# TODO I was very tired when I wrote this and I am not sure if it is correct
def flatten_by_normal_to_level(vec: vec3, normal: vec3, pos: vec3):
    return vec + dot(pos - vec, normal) * normal
