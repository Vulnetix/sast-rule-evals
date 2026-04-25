# Sample for Ruff rule FIX003: line-contains-xxx
# This file is designed to trigger the FIX003 rule.
# Run: ruff check --select FIX003 <this_file>

def speed(distance, time):
    return distance / time  # XXX: Raises ZeroDivisionError for time = 0.
