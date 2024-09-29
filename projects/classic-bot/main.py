# -*- coding: utf-8 -*-
"""Lego remote controlled Classic Bot.

Created on: 20/9/24
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, Remote

from pybricks.parameters import Port, Color, Button

MAX_SPEED = 800
TURN_SPEED = 400


class ClassicBot:

    def __init__(
            self,
            right_motor_port: Port,
            left_motor_port: Port,
            claw_motor_port: Port,
            lifter_motor_port: Port
    ) -> None:
        """Initiate the classic bot.

        Args:
            right_motor_port:
            left_motor_port:
        """
        self.hub = InventorHub()
        self.right_motor = Motor(right_motor_port)
        self.left_motor = Motor(left_motor_port)
        self.claw_motor = Motor(claw_motor_port)
        self.lifter_motor = Motor(lifter_motor_port)
        self.rc = None
        self.connect_radio_control()

    def connect_radio_control(self) -> None:
        """Connect radio control to hub"""
        self.hub.light.on(Color.YELLOW)
        self.rc = Remote()
        self.hub.light.on(Color.GREEN)
        self.rc.light.on(Color.GREEN)

    @staticmethod
    def check_stop(pressed: tuple[Button]) -> bool:
        """Turn off the program

        Args:
            pressed: tuple containing the pressed buttons.

        Returns:
            True if ceter button was pressed, otherwise False
        """
        return not Button.CENTER in pressed

    def move_forward(self, speed: int) -> None:
        self.left_motor.run(-speed)
        self.right_motor.run(speed)

    def move_backward(self, speed: int) -> None:
        self.left_motor.run(speed)
        self.right_motor.run(-speed)

    def move_left(self, speed: int) -> None:
        self.left_motor.run(speed)
        self.right_motor.run(speed)

    def move_right(self, speed: int) -> None:
        self.left_motor.run(-speed)
        self.right_motor.run(-speed)

    def open_claw(self, speed: int) -> None:
        self.claw_motor.run(speed)

    def close_claw(self, speed: int) -> None:
        self.claw_motor.run(-speed)

    def lifter_up(self, speed: int) -> None:
        self.lifter_motor.run(-speed)

    def lifter_down(self, speed: int) -> None:
        self.lifter_motor.run(speed)

    def start(self) -> None:
        """Starts the robot."""
        self.hub.speaker.beep()
        pressed = self.rc.buttons.pressed()

        while self.check_stop(pressed):
            pressed = self.rc.buttons.pressed()

            if Button.LEFT_PLUS in pressed and Button.RIGHT not in pressed:
                self.move_forward(speed=MAX_SPEED)

            elif Button.LEFT_MINUS in pressed and Button.RIGHT not in pressed:
                self.move_backward(speed=MAX_SPEED)

            elif Button.RIGHT_PLUS in pressed and Button.LEFT not in pressed:
                self.move_left(speed=TURN_SPEED)

            elif Button.RIGHT_MINUS in pressed and Button.LEFT not in pressed:
                self.move_right(speed=TURN_SPEED)

            elif Button.RIGHT in pressed and Button.LEFT_PLUS in pressed:
                self.lifter_up(speed=400)

            elif Button.RIGHT in pressed and Button.LEFT_MINUS in pressed:
                self.lifter_down(speed=400)

            elif Button.LEFT in pressed and Button.RIGHT_PLUS in pressed:
                self.open_claw(speed=400)

            elif Button.LEFT in pressed and Button.RIGHT_MINUS in pressed:
                self.close_claw(speed=400)

            else:
                self.claw_motor.stop()
                self.left_motor.stop()
                self.right_motor.stop()
                self.lifter_motor.stop()

        self.rc.light.off()


if __name__ == "__main__":
    classic_bot = ClassicBot(
        right_motor_port=Port.B,
        left_motor_port=Port.A,
        claw_motor_port=Port.E,
        lifter_motor_port=Port.F,
    )

    classic_bot.start()