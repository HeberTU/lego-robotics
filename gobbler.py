# -*- coding: utf-8 -*-
"""Gobbler script.

Created on: 14/6/23
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pybricks.hubs import InventorHub
from pybricks.parameters import Side, Port, Stop
from pybricks.tools import wait
from pybricks.pupdevices import Motor
from pybricks.geometry import Axis

from src.animations import Face
import urandom


def wake_up(hub: InventorHub, motor: Motor) -> None:
    """Play the animation and set the motors simulating the gobble awaking.

    Args:
        hub: InventorHub
            Inventor hub.
    """
    hub.display.orientation(up=Side.LEFT)
    motor.run_target(
        speed=100,
        target_angle=290,
        then=Stop.BRAKE,
        wait=False
    )
    eyes_animation = [Face.EYES_CLOSE, Face.EYES_OPEN]
    for _ in range(3):
        for icon in eyes_animation:
            hub.display.icon(
                icon=icon
            )
            wait(400)


def waiting_animation(hub: InventorHub, blink_time: int = 100) -> None:
    """Animate gobbler face while waiting for inputs.

    Args:
        hub: InventorHub
            Inventor hub.
        blink_time: int = 100
            ms for blinking action.
    """
    hub.display.icon(
        icon=Face.EYES_OPEN
    )
    wait(
        time=urandom.randrange(
            1000,
            3000,
            500
        )
    )
    for _ in range(urandom.randrange(1, 3, 1)):
        hub.display.icon(
            icon=Face.EYES_CLOSE
        )
        wait(time=blink_time)
        hub.display.icon(
            icon=Face.EYES_OPEN
        )
        wait(time=blink_time)


def wait_for_tapping(hub: InventorHub, motor: Motor):
    """Wait for tapping.

    Args:
        hub: InventorHub
            Inventor hub.
    """

    while True:
        waiting_animation(
            hub=hub
        )
        a_t1 = hub.imu.acceleration(axis=Axis.Y)
        if abs(a_t1) > 150:
            motor.run_target(
                speed=500,
                target_angle=0,
                then=Stop.BRAKE,
                wait=False
            )
            hub.display.icon(
                icon=Face.EYES_ANGRY
            )
            break


def main():
    """Main Script."""
    hub = InventorHub(top_side=-Axis.X, front_side=-Axis.Y)
    motor = Motor(Port.A)
    wake_up(hub=hub, motor=motor)
    wait_for_tapping(hub=hub, motor=motor)
    while True:
        pass


if __name__ == '__main__':
    main()