# -*- coding: utf-8 -*-
"""This module contains a set of functions to make two motors act as walking
legs.

Created on: 1/7/23
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pybricks.pupdevices import Motor
from pybricks.tools import wait
from src.utils import get_waiting_time_to_finish_rotation


def set_legs_to_initial_position(
        right_leg: Motor,
        left_leg: Motor,
        speed: int,
        initial_angle: int = -90
) -> None:
    """Set legs to the initial position to do any movement.

        The initial position is one foot completely forward and the other
        completely backward.

    Args:
        right_leg: Motor
            Right leg motor.
        left_leg: Motor
            Left leg motor
        speed: int
            degrees / seconds
        initial_angle:
            Initial angle to rotate.
    """

    right_rotation_angle = (initial_angle - right_leg.angle())
    left_rotation_angle = (initial_angle - left_leg.angle())

    right_leg.run_angle(
        speed=speed,
        rotation_angle=right_rotation_angle,
        wait=False
    )

    left_leg.run_angle(
        speed=speed,
        rotation_angle=left_rotation_angle,
        wait=False
    )

    time_to_wait = get_waiting_time_to_finish_rotation(
        speed=speed,
        rotation_angle=max(
            abs(right_rotation_angle),
            abs(left_rotation_angle)
        )
    )

    wait(time_to_wait + 100)

    right_leg.reset_angle()
    left_leg.reset_angle()


def walk(
        right_leg: Motor,
        left_leg: Motor,
        speed: int,
        forward: bool = True
) -> None:
    """

    Args:
        right_leg: Motor
            Right leg motor.
        left_leg: Motor
            Left leg motor.
        speed: int
            degrees / seconds.
        forward: bool = True
            If True, the walking movement will be forward.
    """
    direction = -1 if forward else 1

    right_leg.run(
        speed=speed * direction
    )
    left_leg.run(
        speed=speed * -direction
    )


def turn(
        right_leg: Motor,
        left_leg: Motor,
        speed: int,
        left: bool = True
) -> None:
    """Turn into the provideddirection

    Args:
        right_leg: Motor
            Right leg motor.
        left_leg: Motor
            Left leg motor.
        speed: int
            degrees / seconds.
        left: bool = True
            If true, the turn will be in the left direction.
    """
    rotation_angle = 180

    direction = -1 if left else 1

    wating_to_finish = get_waiting_time_to_finish_rotation(
        speed=speed,
        rotation_angle=rotation_angle
    )

    left_leg.run_angle(
        speed=speed * -direction,
        rotation_angle=rotation_angle,
        wait=False
    )
    right_leg.run_angle(
        speed=speed * -direction,
        rotation_angle=rotation_angle,
        wait=False
    )
    wait(wating_to_finish + 200)

    # One step forward to balance
    left_leg.run_angle(
        speed=speed * -direction,
        rotation_angle=rotation_angle,
        wait=False
    )

    right_leg.run_angle(
        speed=speed * direction,
        rotation_angle=rotation_angle,
        wait=False
    )
    wait(wating_to_finish + 200)


def turn_left_by_n_steps(
        right_leg: Motor,
        left_leg: Motor,
        speed: int,
        steps: int
) -> None:
    """Turn left to n steps.

    Args:
        right_leg: Motor
            Right leg motor.
        left_leg: Motor
            Left leg motor.
        speed: int
            degrees / seconds.
        steps: int
            Number of steps to turn, each step is equivalent to 80 deg turn.
    """
    left_leg.stop()
    right_leg.stop()

    left_leg.reset_angle()
    right_leg.reset_angle()

    set_legs_to_initial_position(
        right_leg=right_leg,
        left_leg=left_leg,
        speed=300,
    )

    for i in range(steps):
        turn(
            right_leg=right_leg,
            left_leg=left_leg,
            speed=speed
        )

    for leg in [right_leg, left_leg]:
        leg.reset_angle()

    set_legs_to_initial_position(
        right_leg=right_leg,
        left_leg=left_leg,
        speed=300,
    )