# Sample for Ruff rule A003: builtin-attribute-shadowing
# This file is designed to trigger the A003 rule.
# Run: ruff check --select A003 <this_file>

class Class:
    @staticmethod
    def list() -> None:
        pass

    @staticmethod
    def repeat(value: int, times: int) -> list[int]:
        return [value] * times
