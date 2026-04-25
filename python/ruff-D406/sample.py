# Sample for Ruff rule D406: missing-new-line-after-section-name
# This file is designed to trigger the D406 rule.
# Run: ruff check --select D406 <this_file>

# The `Parameters`, `Returns` and `Raises` section headers are all followed
# by a colon in this function's docstring:
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.

    Parameters:
    -----------
    distance : float
        Distance traveled.
    time : float
        Time spent traveling.

    Returns:
    --------
    float
        Speed as distance divided by time.

    Raises:
    -------
    FasterThanLightError
        If speed is greater than the speed of light.
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
