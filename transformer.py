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
    turn_by_n_steps,
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


def calibrate_robot(
    torso: Motor
) -> None:

    print(f" Torso initial angle {torso.angle()}")

    # torso.run_time(
    #     speed=-100,
    #     time=1000
    # )

    torso.run(
        speed=50
    )
    while not torso.stalled():
        wait(5)

    torso.stop()
    torso.reset_angle()
    print(f" Torso final angle {torso.angle()}")


def main():
    """Main script"""
    is_distance_sensor_connected: bool = False
    do_calibration: bool = False

    hub = InventorHub()
    print(f"Hub charger status {hub.battery.voltage()}")
    if is_distance_sensor_connected:
        eyes = UltrasonicSensor(port=Port.D)
    else:
        class MockEyes:

            def __init__(self, time_to_wait: int):
                pass
            def distance(self) -> int:
                wait(8000)
                return 10

        eyes = MockEyes()

    torso = Motor(port=Port.E)

    right_leg, left_leg = initialize_robot(
        right_leg_port=Port.A,
        left_leg_port=Port.B,
    )

    if do_calibration:
        calibrate_robot(
            torso=torso
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

        turn_by_n_steps(
            right_leg=right_leg,
            left_leg=left_leg,
            speed=200,
            steps=6,
            left=False,
        )


if __name__ == '__main__':
    # pybricksdev run ble transformer.py
    main()
