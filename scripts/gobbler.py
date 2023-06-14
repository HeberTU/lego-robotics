# -*- coding: utf-8 -*-
"""Gobbler script.

Created on: 14/6/23
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pybricks.hubs import InventorHub
from pybricks.parameters import Icon, Side
from pybricks.tools import wait


def wake_up(hub: InventorHub) -> None:
    """Play the animation and set the motors simulating the gobble awaking.

    Args:
        hub: InventorHub
            Inventor hub.
    """
    hub.display.orientation(up=Side.LEFT)

    eyes_closed = (
            Icon.EYE_LEFT_BROW
            + Icon.EYE_RIGHT_BROW
    )
    eyes_opened = (
            Icon.EYE_LEFT_BROW
            + Icon.EYE_RIGHT_BROW
            + Icon.EYE_LEFT_BROW_UP
            + Icon.EYE_RIGHT_BROW_UP
    )
    eyes_animation = [eyes_closed, eyes_opened]
    for _ in range(5):
        for icon in eyes_animation:
            hub.display.icon(
                icon=icon
            )
            wait(400)


def main():
    """Main Script."""
    hub = InventorHub()
    wake_up(hub=hub)


if __name__ == '__main__':
    main()