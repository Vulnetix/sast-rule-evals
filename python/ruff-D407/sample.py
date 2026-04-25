# Sample for Ruff rule D407: missing-dashed-underline-after-section
# This file is designed to trigger the D407 rule.
# Run: ruff check --select D407 <this_file>

def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Parameters

    distance : float
        Distance traveled.
    time : float
        Time spent traveling.

    Returns

    float
        Speed as distance divided by time.

    Raises

    FasterThanLightError
        If speed is greater than the speed of light.
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
