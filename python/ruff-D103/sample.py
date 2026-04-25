# Sample for Ruff rule D103: undocumented-public-function
# This file is designed to trigger the D103 rule.
# Run: ruff check --select D103 <this_file>

def calculate_speed(distance: float, time: float) -> float:
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
