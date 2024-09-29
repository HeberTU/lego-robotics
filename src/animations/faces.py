# -*- coding: utf-8 -*-
"""Face module.

Created on: 16/6/23
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pybricks.tools import Matrix

ON = 100
OFF = 0


class Face:
    """Classe used to represent custom face animations."""

    EYES_OPEN: Matrix = Matrix(
        [
            [OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF],
            [ON, ON, OFF, ON, ON],
            [ON, ON, OFF, ON, ON],
            [ON, ON, OFF, ON, ON],
        ]
    )

    EYES_CLOSE: Matrix = Matrix(
        [
            [OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF],
            [ON, ON, OFF, ON, ON],
            [OFF, OFF, OFF, OFF, OFF],
        ]
    )

    EYES_ANGRY = Matrix(
        [
            [ON, OFF, OFF, OFF, ON],
            [OFF, ON, OFF, ON, OFF],
            [OFF, OFF, OFF, OFF, OFF],
            [ON, ON, OFF, ON, ON],
            [ON, ON, OFF, ON, ON],
        ]
    )
