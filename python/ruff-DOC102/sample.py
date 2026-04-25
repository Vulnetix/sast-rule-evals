# Sample for Ruff rule DOC102: docstring-extraneous-parameter
# This file is designed to trigger the DOC102 rule.
# Run: ruff check --select DOC102 <this_file>

def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Args:
        distance: Distance traveled.
        time: Time spent traveling.
        acceleration: Rate of change of speed.

    Returns:
        Speed as distance divided by time.
    """
    return distance / time
