from math import sqrt

from rlbot.utils.game_state_util import Vector3


class vec3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"vec3({self.x}, {self.y}, {self.z})"

    def __add__(self, other: "vec3") -> "vec3":
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "vec3") -> "vec3":
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, k: float) -> "vec3":
        return vec3(self.x * k, self.y * k, self.z * k)

    def __rmul__(self, k: float) -> "vec3":
        return self.__mul__(k)

    def __truediv__(self, k: float) -> "vec3":
        return vec3(self.x / k, self.y / k, self.z / k)

    def norm(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def unit(self) -> "vec3":
        return self / self.norm()

    def done(self) -> Vector3:
        return Vector3(self.x, self.y, self.z)

    def floor(self) -> "vec3":
        return vec3(self.x, self.y, 0.0)

    def dot(self, other: "vec3") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z
