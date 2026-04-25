# Sample for Ruff rule D408: missing-section-underline-after-name
# This file is designed to trigger the D408 rule.
# Run: ruff check --select D408 <this_file>

def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Parameters

    ----------
    distance : float
        Distance traveled.
    time : float
        Time spent traveling.

    Returns

    -------
    float
        Speed as distance divided by time.

    Raises

    ------
    FasterThanLightError
        If speed is greater than the speed of light.
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
