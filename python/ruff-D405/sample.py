# Sample for Ruff rule D405: non-capitalized-section-name
# This file is designed to trigger the D405 rule.
# Run: ruff check --select D405 <this_file>

def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    args:
        distance: Distance traveled.
        time: Time spent traveling.

    returns:
        Speed as distance divided by time.

    raises:
        FasterThanLightError: If speed is greater than the speed of light.
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
