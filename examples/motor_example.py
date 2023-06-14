# -*- coding: utf-8 -*-
"""
Example script on how to operate a motor while using config from a module.

Created on: 14/6/23
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

from example_config.lego_constants import SPEED


def main():
    """Main function."""
    # Initialize a motor on port A.
    example_motor = Motor(port=Port.A)

    # Make the motor run clockwise at 500 degrees per second.
    example_motor.run(speed=SPEED)

    # Wait for three seconds.
    wait(time=3000)

    # Make the motor run counterclockwise at 500 degrees per second.
    example_motor.run(speed=-SPEED)

    # Wait for three seconds.
    wait(time=3000)


if __name__ == '__main__':
    main()
