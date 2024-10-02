"""Hub basic control.

Created on: 2024-10-02
@author: Heber Trujillo <heber.trj.urt@gmail.com>
License: MIT
"""
from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait


class BasicMotorControl:
    """Basic motor control."""

    def __init__(self) -> None:
        """Initialize the basic motor."""
        self.hub = InventorHub()
        self.motor: Motor = Motor(port=Port.A)
        self.speed: int = 0
        self.last_pressed: set = set()
        self.increase: int = 100

    def update_motor_move(self, button: Button) -> None:
        """Update the motor speed.

        Args:
            button: button pressed.

        Returns:
            None
        """
        if button == Button.LEFT:
            self.speed += self.increase
        elif button == Button.RIGHT:
            self.speed -= self.increase

    def start(self) -> None:
        """Start the robot operation."""
        while True:
            current_pressed = set(self.hub.buttons.pressed())
            new_presses = current_pressed - self.last_pressed

            print(f"Speed: {self.speed}")

            if Button.LEFT in new_presses:
                self.update_motor_move(button=Button.LEFT)
                self.motor.run(self.speed)

            elif Button.RIGHT in new_presses:
                self.update_motor_move(button=Button.RIGHT)
                self.motor.run(self.speed)

            if self.speed == 0:
                self.motor.stop()

            self.last_pressed = current_pressed
            wait(100)  # Small delay to avoid excessive CPU usage


if __name__ == "__main__":
    basic_motor_control = BasicMotorControl()
    basic_motor_control.start()
