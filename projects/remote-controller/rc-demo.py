# -*- coding: utf-8 -*-
"""Lego remote controller script.

Created on: 20/9/24
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, Remote
from pybricks.parameters import Port, Color, Button

MAX_SPEED = 720


def main():

    hub = InventorHub()
    motor = Motor(Port.A)

    speed = MAX_SPEED

    hub.light.on(Color.YELLOW)
    rc = Remote()
    hub.light.on(Color.GREEN)
    rc.light.on(Color.GREEN)

    print("Hub and remote control connected!")


    while True:
        pressed = rc.buttons.pressed()

        if Button.LEFT_PLUS in pressed:
            motor.run(speed)
        elif Button.LEFT_MINUS in pressed:
            motor.run(-speed)
        else:
            motor.stop()



if __name__ == "__main__":
    main()