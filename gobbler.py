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


def wake_up(hub: InventorHub) -> None:
    """Play the animation and set the motors simulating the gobble awaking.

    Args:
        hub: InventorHub
            Inventor hub.
    """
    hub.display.orientation(up=Side.LEFT)


    eyes_animation = [Face.EYES_CLOSE, Face.EYES_OPEN]
    for _ in range(5):
        for icon in eyes_animation:
            hub.display.icon(
                icon=icon
            )
            wait(400)


def wait_for_tapping(hub: InventorHub):

    while True:
        hub.display.icon(
            icon=Face.EYES_OPEN
        )
        wait(400)
        hub.display.icon(
            icon=Face.EYES_CLOSE
        )
        wait(100)
        hub.display.icon(
            icon=Face.EYES_OPEN
        )
        wait(100)
        hub.display.icon(
            icon=Face.EYES_CLOSE
        )


def main():
    """Main Script."""
    hub = InventorHub()
    wake_up(hub=hub)
    wait_for_tapping(hub=hub)


if __name__ == '__main__':
    main()