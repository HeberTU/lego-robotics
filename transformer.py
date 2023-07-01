# -*- coding: utf-8 -*-
"""

Created on: 26/6/23
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
import umath
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port

from pybricks.tools import wait


def initialize_robot(
        right_leg_port: Port,
        left_leg_port: Port,
):
    """

    Args:
        right_leg_port: Port
        left_leg_port: Port
    Returns:

    """
    legs = (
        Motor(
            port=right_leg_port,
            reset_angle=True
        ),
        Motor(
            port=left_leg_port,
            reset_angle=True
        )
    )

    return legs


def get_waiting_time_to_finish_rotation(
        speed: int,
        rotation_angle: int
) -> int:
    """Get how much time is needed to wait for a motor to rotate the specified
    degrees.

    Args:
        speed: int
            degrees / seconds
        rotation_angle: int
            number of degrees to rotate

    Returns:
        int:
            Number of milliseconds to wait.
    """
    return umath.ceil((rotation_angle / speed) * 1000)


def set_legs_to_initial_position(
        right_leg: Motor,
        left_leg: Motor,
        speed: int,
        initial_angle: int = -90
) -> None:
    """Set legs to the initial position to do any movement.

        The initial position is one foot completely forward and the other
        completely backward.

    Args:
        right_leg: Motor
            Right leg motor.
        left_leg: Motor
            Left leg motor
        speed: int
            degrees / seconds
        initial_angle:
            Initial angle to rotate.
    """

    right_rotation_angle = (right_leg.angle() + initial_angle)
    left_rotation_angle = (left_leg.angle() + initial_angle)

    right_leg.run_angle(
        speed=-speed,
        rotation_angle=right_rotation_angle,
        wait=False
    )

    left_leg.run_angle(
        speed=-speed,
        rotation_angle=left_rotation_angle,
        wait=False
    )

    time_to_wait = get_waiting_time_to_finish_rotation(
        speed=speed,
        rotation_angle=max(
            abs(right_rotation_angle),
            abs(left_rotation_angle)
        )
    )

    wait(time_to_wait)

    right_leg.reset_angle()
    left_leg.reset_angle()


def walk(
    right_leg: Motor,
    left_leg: Motor,
    speed: int,
    forward: bool = True
) -> None:
    """

    Args:
        right_leg: Motor
            Right leg motor.
        left_leg: Motor
            Left leg motor.
        speed: int
            degrees / seconds.
        forward: bool = True
            If True, the walking movement will be forward.
    """
    direction = -1 if forward else 1

    right_leg.run(
        speed=speed * direction
    )
    left_leg.run(
        speed=speed * -direction
    )

def turn_left_by_n_steps(
        right_leg: Motor,
        left_leg: Motor,
        steps: int
) -> None:
    left_leg.stop()
    right_leg.stop()

    left_leg.reset_angle()
    right_leg.reset_angle()

    for leg in [right_leg, left_leg]:
        leg.stop()
        leg.reset_angle()

        leg.run_target(
            speed=300,
            target_angle=-90,
            wait=False
        )

    wait(1000)

    print(f"Right Angle {right_leg.angle()}")
    print(f"Left Angle {right_leg.angle()}")
    for i in range(steps):
        print(f"rotation {i}")
        left_leg.run_angle(
            speed=250,
            rotation_angle=180,
            wait=False
        )

        right_leg.run_angle(
            speed=250,
            rotation_angle=180,
            wait=False
        )
        wait(720)
        left_leg.run_angle(
            speed=250,
            rotation_angle=180,
            wait=False
        )

        right_leg.run_angle(
            speed=-250,
            rotation_angle=180,
            wait=False
        )
        wait(720)
        print(f"Right Angle {right_leg.angle()}")
        print(f"Left Angle {right_leg.angle()}")

    for leg in [right_leg, left_leg]:
        leg.reset_angle()


def test_motors(right_leg: Motor) -> None:
    print(f"Initial angle: {right_leg.angle()}")
    right_leg.run_angle(
        speed=200,
        rotation_angle=360
    )


def main():
    """Main script"""
    hub = InventorHub()
    eyes = UltrasonicSensor(Port.D)

    right_leg, left_leg = initialize_robot(
        right_leg_port=Port.A,
        left_leg_port=Port.B,
    )

    set_legs_to_initial_position(
        right_leg=right_leg,
        left_leg=left_leg,
        speed=300,
    )

    while True:

        walk(
            right_leg=right_leg,
            left_leg=left_leg,
            speed=200,
            forward=True
        )
    #
    #     while eyes.distance() > 50:
    #         wait(20)
    #
    #     turn_left_by_n_steps(
    #         right_leg=right_leg,
    #         left_leg=left_leg,
    #         steps=5
    #     )
    #
    #     set_legs_to_initial_position(
    #         right_leg=right_leg,
    #         left_leg=left_leg,
    #         speed=300,
    #     )
    #
    # print(f"Final right angle: {right_leg.angle()}")
    # print(f"Final left angle: {left_leg.angle()}")


if __name__ == '__main__':
    # pybricksdev run ble transformer.py
    main()
