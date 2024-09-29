# -*- coding: utf-8 -*-
"""Demo script.

Created on: 20/9/24
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pybricks.hubs import InventorHub
from pybricks.parameters import Side


def main():
    """Start main function."""
    hub = InventorHub()
    hub.display.orientation(up=Side.TOP)
    hub.speaker.beep()
    hub.display.text("Hello world!")


if __name__ == "__main__":
    # pybricksdev run ble demo.py
    main()
