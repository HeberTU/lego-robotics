"""Lego remote controlled Classic Bot.

Created on: 2024-09-20
@author: Heber Trujillo <heber.trj.urt@gmail.com>
License: MIT
"""
from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Color, Port
from pybricks.pupdevices import Motor, Remote


class Speed:
    """Enum for different speed settings."""

    MAX = 800
    TURN = 400
    CLAW = 400
    LIFTER = 400


class Direction:
    """Enum for movement directions."""

    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4


class MotorPorts:
    """Class to hold motor port configurations."""

    def __init__(
        self, right: Port, left: Port, claw: Port, lifter: Port
    ) -> None:
        """Instantiate a motor port.

        Args:
            right: Right driving wheel
            left: Left driving wheel
            claw: Claw
            lifter:Lifter
        """
        self.right = right
        self.left = left
        self.claw = claw
        self.lifter = lifter


class ClassicBot:
    """ClassicBot: A remote-controlled Lego robot."""

    def __init__(self, motor_ports: MotorPorts) -> None:
        """Initialize the ClassicBot.

        Args:
            motor_ports: MotorPorts object containing port configurations.
        """
        self.hub = InventorHub()
        self.right_motor = Motor(motor_ports.right)
        self.left_motor = Motor(motor_ports.left)
        self.claw_motor = Motor(motor_ports.claw)
        self.lifter_motor = Motor(motor_ports.lifter)
        self._connect_radio_control()

    def _connect_radio_control(self) -> None:
        """Connect radio control to hub."""
        self.hub.light.on(Color.YELLOW)
        self.rc = Remote()
        self.hub.light.on(Color.GREEN)
        self.rc.light.on(Color.GREEN)

    @staticmethod
    def _should_continue(pressed: set[Button]) -> bool:
        """Check if the program should continue running.

        Args:
            pressed: Tuple containing the pressed buttons.

        Returns:
            True if the program should continue, False otherwise.
        """
        return Button.CENTER not in pressed

    def _move(self, direction: int, speed: int) -> None:
        """Move the robot in the specified direction.

        Args:
            direction: Direction enum specifying the movement direction.
            speed: Integer specifying the motor speed.
        """
        right_speed = speed
        left_speed = speed
        if direction in (Direction.FORWARD, Direction.RIGHT):
            left_speed *= -1
        if direction in (Direction.BACKWARD, Direction.RIGHT):
            right_speed *= -1
        self.left_motor.run(left_speed)
        self.right_motor.run(right_speed)

    def _operate_claw(self, speed: int) -> None:
        """Operate the claw.

        Args:
            speed: Integer specifying the claw motor speed (positive to open,
            negative to close).
        """
        self.claw_motor.run(speed)

    def _operate_lifter(self, speed: int) -> None:
        """Operate the lifter.

        Args:
            speed: Integer specifying the lifter motor speed (positive for up,
            negative for down).
        """
        self.lifter_motor.run(-speed)

    def _stop_all_motors(self) -> None:
        """Stop all motors."""
        for motor in (
            self.claw_motor,
            self.left_motor,
            self.right_motor,
            self.lifter_motor,
        ):
            motor.stop()

    def start(self) -> None:
        """Start the robot operation."""
        self.hub.speaker.beep()

        while self._should_continue(self.rc.buttons.pressed()):
            pressed = self.rc.buttons.pressed()

            if Button.LEFT_PLUS in pressed and Button.RIGHT not in pressed:
                self._move(Direction.FORWARD, Speed.MAX)
            elif Button.LEFT_MINUS in pressed and Button.RIGHT not in pressed:
                self._move(Direction.BACKWARD, Speed.MAX)
            elif Button.RIGHT_PLUS in pressed and Button.LEFT not in pressed:
                self._move(Direction.LEFT, Speed.TURN)
            elif Button.RIGHT_MINUS in pressed and Button.LEFT not in pressed:
                self._move(Direction.RIGHT, Speed.TURN)

            elif Button.RIGHT in pressed and Button.LEFT_PLUS in pressed:
                self._operate_lifter(Speed.LIFTER)
            elif Button.RIGHT in pressed and Button.LEFT_MINUS in pressed:
                self._operate_lifter(-Speed.LIFTER)
            elif Button.LEFT in pressed and Button.RIGHT_PLUS in pressed:
                self._operate_claw(Speed.CLAW)
            elif Button.LEFT in pressed and Button.RIGHT_MINUS in pressed:
                self._operate_claw(-Speed.CLAW)
            else:
                self._stop_all_motors()

        self.rc.light.off()


if __name__ == "__main__":
    motor_ports = MotorPorts(
        right=Port.B, left=Port.A, claw=Port.E, lifter=Port.F
    )
    classic_bot = ClassicBot(motor_ports)
    classic_bot.start()
