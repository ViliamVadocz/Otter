from math import copysign
from typing import Union, Optional

from utils.arena.arena import Arena
from rlutilities.linear_algebra import vec2, vec3


class StandardArena(Arena):
    length: float = 5120
    width: float = 4096
    height: float = 2044
    goal_width: float = 892.755

    def find_intermediate(
        self, start: Union[vec2, vec3], end: Union[vec2, vec3]
    ) -> Optional[Union[vec2, vec3]]:
        if abs(start.y) > self.length:
            goal_brim: float = 100
            x: float = copysign(
                min(abs(end.x), self.__class__.goal_width - goal_brim), end.x
            )
            if not hasattr(end, "z"):
                return vec2(x, end.y)
            return vec3(x, end.y, end.z)
        return None
