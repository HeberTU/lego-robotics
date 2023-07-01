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
        speed: int
):
    """

    Args:
        right_leg_port: Port
        left_leg_port: Port
        speed: int
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
    """"""
    # right_leg.reset_angle()
    right_rotation_angle = (right_leg.angle() + initial_angle)

    print(f"Rotation Angle: {right_rotation_angle}")

    right_leg.run_angle(
        speed=-speed,
        rotation_angle=right_rotation_angle,
        wait=False
    )

    right_waiting_ms = umath.ceil((right_rotation_angle / speed) * 1000)
    print(f"waiting time: {right_waiting_ms}")
    wait(right_waiting_ms)

    print(f"Final Angle: {right_leg.angle()}")
    right_leg.reset_angle()
    print(f"Reseted Angle: {right_leg.angle()}")

def walk_forward(right_leg: Motor, left_leg: Motor) -> None:
    """"""
    right_leg.run(
        speed=-200
    )
    left_leg.run(
        speed=200
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
        speed=300
    )

    set_legs_to_initial_position(
        right_leg=right_leg,
        left_leg=left_leg,
        speed=300,
    )

    # while True:
    #
    #     walk_forward(
    #         right_leg=right_leg,
    #         left_leg=left_leg,
    #     )
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
