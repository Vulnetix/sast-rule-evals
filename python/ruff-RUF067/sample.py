# Sample for Ruff rule RUF067: non-empty-init-module
# This file is designed to trigger the RUF067 rule.
# Run: ruff check --select RUF067 <this_file>

"""My module docstring."""


class MyClass:
    def my_method(self): ...
