import math

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket

from util.orientation import Orientation
from util.vec import Vec3


class MyBot(BaseAgent):
    def initialize_agent(self):
        # This runs once before the bot starts up
        self.controller_state = SimpleControllerState()
        self.sign: float = (-1 if self.team else 1)
        self.go_home: bool = False

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        ball_location = Vec3(packet.game_ball.physics.location)

        my_car = packet.game_cars[self.index]
        car_location = Vec3(my_car.physics.location)

        if self.go_home:
            self.go_home = car_location.y * self.sign > -4000
        if not self.go_home:
            self.go_home = car_location.y * self.sign > ball_location.y * self.sign
        # self.go_home &= not packet.game_info.is_kickoff_pause

        goal_location = Vec3(0, 5120 * self.sign, 0)
        target_location = goal_location * -1
        if not self.go_home:
            shoot_factor: float = 0.3
            target_location = ball_location - (
                goal_location - ball_location
            ).normalized * max(
                130,
                car_location.dist(ball_location)
                * shoot_factor
                * (not packet.game_info.is_kickoff_pause),
            )

        # Find the direction of our car using the Orientation class
        car_orientation = Orientation(my_car.physics.rotation)

        steer_correction_radians = find_correction(
            car_orientation.forward, target_location - car_location
        )

        self.controller_state.steer = max(-1, min(1, steer_correction_radians * -3))
        self.controller_state.throttle = math.cos(steer_correction_radians)
        self.controller_state.yaw = self.controller_state.steer * 0.6
        self.controller_state.pitch = car_orientation.pitch * -0.6
        self.controller_state.roll = car_orientation.roll * -0.6
        self.controller_state.boost = (
            self.controller_state.throttle > 0.85 and not my_car.is_super_sonic
        )
        self.controller_state.handbrake = abs(self.controller_state.throttle) < 0.5
        self.controller_state.jump = (
            my_car.has_wheel_contact and abs(steer_correction_radians) > 1
        )
        if not (my_car.has_wheel_contact or my_car.double_jumped):
            dodge: bool = 0 < my_car.physics.velocity.z < 650 / 60
            if dodge:
                self.controller_state.jump = True
                self.controller_state.pitch = -math.cos(steer_correction_radians)
                self.controller_state.yaw = -math.sin(steer_correction_radians)

        draw_debug(self.renderer, my_car, packet.game_ball, str(self.go_home))

        return self.controller_state


def find_correction(current: Vec3, ideal: Vec3) -> float:
    # Finds the angle from current to ideal vector in the xy-plane. Angle will be between -pi and +pi.

    # The in-game axes are left handed, so use -x
    current_in_radians = math.atan2(current.y, -current.x)
    ideal_in_radians = math.atan2(ideal.y, -ideal.x)

    diff = ideal_in_radians - current_in_radians

    # Make sure that diff is between -pi and +pi.
    if abs(diff) > math.pi:
        if diff < 0:
            diff += 2 * math.pi
        else:
            diff -= 2 * math.pi

    return diff


def draw_debug(renderer, car, ball, action_display):
    renderer.begin_rendering()
    # draw a line from the car to the ball
    renderer.draw_line_3d(car.physics.location, ball.physics.location, renderer.white())
    # print the action that the bot is taking
    renderer.draw_string_3d(
        car.physics.location, 2, 2, action_display, renderer.white()
    )
    renderer.end_rendering()
