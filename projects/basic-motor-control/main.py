"""Hub basic control.

Created on: 2024-10-02
@author: Heber Trujillo <heber.trj.urt@gmail.com>
License: MIT
"""
from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Port
from pybricks.pupdevices import Motor


class BasicMotorControl:
    """Basic motor control."""

    def __init__(self) -> None:
        """Initialize the basic motor."""
        self.hub = InventorHub()
        self.motor: Motor = Motor(port=Port.A)
        self.init_speed = 0

    def update_moto_move(self, button: Button) -> None:
        """Update the motor speed.

        Args:
            button: button pressed.

        Returns:
            None
        """
        if button == Button.LEFT:
            self.init_speed += 100
        elif button == Button.RIGHT:
            self.init_speed -= 100

    def start(self) -> None:
        """Start the robot operation."""
        while True:
            pressed = self.hub.buttons.pressed()

            if Button.LEFT or Button.RIGHT in pressed:
                self.update_moto_move(button=Button.LEFT)
                self.motor.run(self.init_speed)

            if self.init_speed == 0:
                self.motor.stop()


if __name__ == "__main__":
    basic_motor_control = BasicMotorControl()
    basic_motor_control.start()
