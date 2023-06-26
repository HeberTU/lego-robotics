# -*- coding: utf-8 -*-
"""

Created on: 26/6/23
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
# from typing import Dict
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
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
        ),
        Motor(
            port=left_leg_port,
        )
    )

    set_legs_to_initial_position(
        right_leg=legs[0],
        left_leg=legs[1],
        speed=speed,
    )

    return legs


def set_legs_to_initial_position(
    right_leg: Motor,
    left_leg: Motor,
    speed: int
) -> None:
    """"""
    legs = (right_leg, left_leg)

    for leg in legs:
        leg.run_target(
            speed=speed,
            target_angle=270,
            wait=True
        )


def walk_forward(right_leg: Motor, left_leg: Motor) -> None:
    """"""
    right_leg.run(
        speed=-200
    )
    left_leg.run(
        speed=200
    )


def main():
    """Main script"""
    hub = InventorHub()

    right_leg, left_leg = initialize_robot(
        right_leg_port=Port.A,
        left_leg_port=Port.B,
        speed=300
    )


    walk_forward(
        right_leg=right_leg,
        left_leg=left_leg,
    )

    while True:

        print(f"right angle: {right_leg.angle()}")
        print(f"left angle: {left_leg.angle()}")
        wait(1000)


if __name__ == '__main__':
    # pybricksdev run ble transformer.py
    main()