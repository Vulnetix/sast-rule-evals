# Sample for Ruff rule D214: overindented-section
# This file is designed to trigger the D214 rule.
# Run: ruff check --select D214 <this_file>

def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

        Args:
            distance: Distance traveled.
            time: Time spent traveling.

    Returns:
        Speed as distance divided by time.

    Raises:
        FasterThanLightError: If speed is greater than the speed of light.
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
