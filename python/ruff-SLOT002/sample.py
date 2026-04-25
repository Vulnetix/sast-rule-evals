# Sample for Ruff rule SLOT002: no-slots-in-namedtuple-subclass
# This file is designed to trigger the SLOT002 rule.
# Run: ruff check --select SLOT002 <this_file>

from typing import NamedTuple

class Point(NamedTuple):  # SLOT002: NamedTuple subclass
    x: float
    y: float

    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5

