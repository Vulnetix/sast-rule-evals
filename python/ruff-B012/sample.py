# Sample for Ruff rule B012: jump-statement-in-finally
# This file is designed to trigger the B012 rule.
# Run: ruff check --select B012 <this_file>

def speed(distance, time):
    try:
        return distance / time
    except ZeroDivisionError:
        raise ValueError("Time cannot be zero")
    finally:
        return 299792458  # `ValueError` is silenced
