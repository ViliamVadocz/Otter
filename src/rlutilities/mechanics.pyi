from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import rlutilities.simulation
from rlutilities.linear_algebra import *
__all__  = [
"Aerial",
"Boostdash",
"Dodge",
"Drive",
"FollowPath",
"Jump",
"Reorient",
"ReorientML",
"Wavedash"
]
class Aerial():
    boost_accel = 1060.0
    boost_per_second = 30.0
    max_speed = 2300.0
    throttle_accel = 66.66667175292969

    def __init__(self, arg0: rlutilities.simulation.Car) -> None: ...
    def is_viable(self) -> bool: ...
    def simulate(self) -> rlutilities.simulation.Car: ...
    def step(self, arg0: float) -> None: ...

    angle_threshold: float
    arrival_time: float
    controls: rlutilities.simulation.Input
    double_jump: bool
    finished: bool
    reorient_distance: float
    target_orientation: mat3
    target_position: vec3
    up: vec3
    pass
class Boostdash():

    def __init__(self, arg0: rlutilities.simulation.Car) -> None: ...
    def step(self, arg0: float) -> None: ...

    controls: rlutilities.simulation.Input
    finished: bool
    pass
class Dodge():
    forward_torque = 224.0
    input_threshold = 0.5
    side_torque = 260.0
    timeout = 1.25
    torque_time = 0.6499999761581421
    z_damping = 0.3499999940395355
    z_damping_end = 0.20999999344348907
    z_damping_start = 0.15000000596046448

    def __init__(self, arg0: rlutilities.simulation.Car) -> None: ...
    def simulate(self) -> rlutilities.simulation.Car: ...
    def step(self, arg0: float) -> None: ...

    controls: rlutilities.simulation.Input
    delay: float
    direction: vec2
    finished: bool
    jump_duration: float
    preorientation: mat3
    timer: float
    pass
class Drive():
    boost_accel = 991.6669921875
    brake_accel = 3500.0
    coasting_accel = 525.0
    max_speed = 2300.0
    max_throttle_speed = 1410.0

    def __init__(self, arg0: rlutilities.simulation.Car) -> None: ...
    @staticmethod
    def max_turning_curvature(arg0: float) -> float: ...
    @staticmethod
    def max_turning_speed(arg0: float) -> float: ...
    def step(self, arg0: float) -> None: ...
    @staticmethod
    def throttle_accel(arg0: float) -> float: ...

    controls: rlutilities.simulation.Input
    finished: bool
    reaction_time: float
    speed: float
    target: vec3
    pass
class FollowPath():

    def __init__(self, arg0: rlutilities.simulation.Car) -> None: ...
    def calculate_plan(self, arg0: rlutilities.simulation.Curve, arg1: float, arg2: float) -> None: ...
    def step(self, arg0: float) -> None: ...

    arrival_speed: float
    arrival_time: float
    controls: rlutilities.simulation.Input
    finished: bool
    path: rlutilities.simulation.Curve
    pass
class Jump():
    acceleration = 1458.333251953125
    max_duration = 0.20000000298023224
    min_duration = 0.02500000037252903
    speed = 291.6669921875

    def __init__(self, arg0: rlutilities.simulation.Car) -> None: ...
    def simulate(self) -> rlutilities.simulation.Car: ...
    def step(self, arg0: float) -> None: ...

    controls: rlutilities.simulation.Input
    duration: float
    finished: bool
    pass
class Reorient():

    def __init__(self, arg0: rlutilities.simulation.Car) -> None: ...
    def simulate(self) -> rlutilities.simulation.Car: ...
    def step(self, arg0: float) -> None: ...

    alpha: vec3
    controls: rlutilities.simulation.Input
    eps_omega: float
    eps_phi: float
    finished: bool
    horizon_time: float
    target_orientation: mat3
    pass
class ReorientML():

    def __init__(self, arg0: rlutilities.simulation.Car) -> None: ...
    def simulate(self) -> rlutilities.simulation.Car: ...
    def step(self, arg0: float) -> None: ...

    controls: rlutilities.simulation.Input
    eps_phi: float
    finished: bool
    target_orientation: mat3
    pass
class Wavedash():

    def __init__(self, arg0: rlutilities.simulation.Car) -> None: ...
    def step(self, arg0: float) -> None: ...

    controls: rlutilities.simulation.Input
    direction: vec2
    finished: bool
    pass