# Sample for Ruff rule PLE1519: singledispatch-method
# This file is designed to trigger the PLE1519 rule.
# Run: ruff check --select PLE1519 <this_file>

from functools import singledispatch


class Class:
    @singledispatch
    def method(self, arg): ...
