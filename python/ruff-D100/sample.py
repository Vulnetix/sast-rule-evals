# Sample for Ruff rule D100: undocumented-public-module
# This file is designed to trigger the D100 rule.
# Run: ruff check --select D100 <this_file>

class FasterThanLightError(ZeroDivisionError): ...


def calculate_speed(distance: float, time: float) -> float: ...
