# Sample for Ruff rule SLOT001: no-slots-in-tuple-subclass
# This file is designed to trigger the SLOT001 rule.
# Run: ruff check --select SLOT001 <this_file>

class MyTuple(tuple):  # SLOT001: no __slots__
    def sum(self):
        return sum(self)

