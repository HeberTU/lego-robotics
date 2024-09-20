# -*- coding: utf-8 -*-
"""Demo script.

Created on: 20/9/24
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pybricks.hubs import InventorHub
from pybricks.tools import wait
from pybricks.parameters import Side

from src.animations import Characters

def main():

    hub = InventorHub()
    hub.display.orientation(up=Side.TOP)
    hub.display.icon(
        icon=Characters.OK
    )
    wait(1000)





if __name__ == '__main__':
    # pybricksdev run ble demo.py
    main()