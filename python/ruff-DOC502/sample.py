# Sample for Ruff rule DOC502: docstring-extraneous-exception
# This file is designed to trigger the DOC502 rule.
# Run: ruff check --select DOC502 <this_file>

def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Args:
        distance: Distance traveled.
        time: Time spent traveling.

    Returns:
        Speed as distance divided by time.

    Raises:
        ZeroDivisionError: Divided by zero.
    """
    return distance / time
