import enum
from dataclasses import dataclass

@dataclass
class Color(enum.Enum):  # RUF049: dataclass applied to enum
    RED = 1
