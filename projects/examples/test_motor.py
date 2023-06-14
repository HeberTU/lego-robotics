# -*- coding: utf-8 -*-
"""

Created on: 14/6/23
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait


def main():
    # Initialize a motor on port A.
    example_motor = Motor(port=Port.A)

    # Make the motor run clockwise at 500 degrees per second.
    example_motor.run(speed=500)

    # Wait for three seconds.
    wait(time=3000)

    # Make the motor run counterclockwise at 500 degrees per second.
    example_motor.run(speed=-500)

    # Wait for three seconds.
    wait(time=3000)


main()
