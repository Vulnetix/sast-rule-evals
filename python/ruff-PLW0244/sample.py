# Sample for Ruff rule PLW0244: redefined-slots-in-subclass
# This file is designed to trigger the PLW0244 rule.
# Run: ruff check --select PLW0244 <this_file>

class Base:
    __slots__ = ("a", "b")


class Subclass(Base):
    __slots__ = ("a", "d")  # slot "a" redefined
