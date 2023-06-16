# -*- coding: utf-8 -*-
"""Gobbler script.

Created on: 14/6/23
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pybricks.hubs import InventorHub
from pybricks.parameters import Side
from pybricks.tools import wait

from src.animations import Face
import urandom

def wake_up(hub: InventorHub) -> None:
    """Play the animation and set the motors simulating the gobble awaking.

    Args:
        hub: InventorHub
            Inventor hub.
    """
    hub.display.orientation(up=Side.LEFT)

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
            3000,
            6000,
            1000
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


def wait_for_tapping(hub: InventorHub):
    """Wait for tapping.

    Args:
        hub: InventorHub
            Inventor hub.
    """
    while True:
        waiting_animation(
            hub=hub
        )


def main():
    """Main Script."""
    hub = InventorHub()
    wake_up(hub=hub)
    wait_for_tapping(hub=hub)


if __name__ == '__main__':
    main()