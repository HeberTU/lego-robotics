from pybricks.geometry import Matrix

OON = 100
OFF = 0


class Characters:

    OK: Matrix = Matrix(
        [
            [OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OON],
            [OFF, OON, OFF, OON, OFF],
            [OFF, OFF, OON, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF],
        ]
    )