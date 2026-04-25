# Sample for Ruff rule DOC501: docstring-missing-exception
# This file is designed to trigger the DOC501 rule.
# Run: ruff check --select DOC501 <this_file>

class FasterThanLightError(ArithmeticError): ...


def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Args:
        distance: Distance traveled.
        time: Time spent traveling.

    Returns:
        Speed as distance divided by time.
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
