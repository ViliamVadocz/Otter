from math import copysign
from typing import Union, Optional

from rlutilities.linear_algebra import vec2, vec3


class Arena:
    """
    All dimensions measure half of the arena.
    """

    length: float = 0
    width: float = 0
    height: float = 0

    def find_intermediate(
        self, start: Union[vec2, vec3], end: Union[vec2, vec3]
    ) -> Optional[Union[vec2, vec3]]:
        return None

    def clamp(self, vector: Union[vec2, vec3]) -> Union[vec2, vec3]:
        x: float = copysign(min(abs(vector.x), self.__class__.width), vector.x)
        y: float = copysign(min(abs(vector.y), self.__class__.length), vector.y)
        if not hasattr(vector, "z"):
            return vec2(x, y)
        return vec3(x, y, max(0, min(self.__class__.height, vector.z)))
