# -*- coding: utf-8 -*-
"""

Created on: 16/6/23
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pybricks.geometry import Matrix

ON = 100
OFF = 0


class Face:
    """This classe  is used to represent custom face animations."""

    EYES_OPEN: Matrix = Matrix(
        [
            [OFF, OFF, OFF, OFF, OFF],
            [ON,  ON,  OFF, ON,  ON],
            [ON,  ON,  OFF, ON,  ON],
            [ON,  ON, OFF,  ON,  ON],
            [OFF, OFF, OFF, OFF, OFF],
        ]
    )

    EYES_CLOSE: Matrix = Matrix(
        [
            [OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF],
            [ON,  ON,  OFF, ON,  ON],
            [OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF],
        ]
    )

