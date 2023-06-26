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
    right_leg_port: Port, left_leg_port: Port
):
    """

    Args:
        right_leg_port:
        left_leg_port:

    Returns:

    """
    right_leg = Motor(
        port=right_leg_port,
    )

    left_leg = Motor(
        port=left_leg_port,
    )

    return right_leg, left_leg


def main():
    """Main script"""
    hub = InventorHub()

    legs = initialize_robot(
        right_leg_port=Port.A,
        left_leg_port=Port.B
    )

    while True:

        print(f"right angle: {legs.get('right').angle()}")
        print(f"left angle: {legs.get('left').angle()}")
        wait(1000)


if __name__ == '__main__':
    # pybricksdev run ble transformer.py
    main()