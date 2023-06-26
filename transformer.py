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

    for leg in legs:
        leg.run_target(
            speed=speed,
            target_angle=270,
            wait=False
        )

    return legs


def main():
    """Main script"""
    hub = InventorHub()

    right_leg, left_leg = initialize_robot(
        right_leg_port=Port.A,
        left_leg_port=Port.B,
        speed=100
    )

    while True:

        print(f"right angle: {right_leg.angle()}")
        print(f"left angle: {left_leg.angle()}")
        wait(1000)


if __name__ == '__main__':
    # pybricksdev run ble transformer.py
    main()