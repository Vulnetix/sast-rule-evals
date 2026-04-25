from typing import Literal

x: Literal[Literal[1, 2], 3]  # RUF041: unnecessary nested Literal
