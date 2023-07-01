# -*- coding: utf-8 -*-
"""

Created on: 26/6/23
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port

from pybricks.tools import wait

from src.movement.walking import (
    set_legs_to_initial_position,
    walk,
    turn_left_by_n_steps
)


def initialize_robot(
        right_leg_port: Port,
        left_leg_port: Port,
):
    """Initialize robot legs.

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


def main():
    """Main script"""
    _ = InventorHub()
    eyes = UltrasonicSensor(Port.D)

    right_leg, left_leg = initialize_robot(
        right_leg_port=Port.A,
        left_leg_port=Port.B,
    )

    set_legs_to_initial_position(
        right_leg=right_leg,
        left_leg=left_leg,
        speed=200,
    )

    while True:

        walk(
            right_leg=right_leg,
            left_leg=left_leg,
            speed=200,
            forward=True
        )

        while eyes.distance() > 50:
            wait(20)

        turn_left_by_n_steps(
            right_leg=right_leg,
            left_leg=left_leg,
            speed=200,
            steps=5
        )


if __name__ == '__main__':
    # pybricksdev run ble transformer.py
    main()
