# -*- coding: utf-8 -*-
"""

Created on: 1/7/23
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
import umath


def get_waiting_time_to_finish_rotation(
        speed: int,
        rotation_angle: int
) -> int:
    """Get how much time is needed to wait for a motor to rotate the specified
    degrees.

    Args:
        speed: int
            degrees / seconds
        rotation_angle: int
            number of degrees to rotate

    Returns:
        int:
            Number of milliseconds to wait.
    """
    return umath.ceil((rotation_angle / speed) * 1000)