# Sample for Ruff rule SIM105: suppressible-exception
# This file is designed to trigger the SIM105 rule.
# Run: ruff check --select SIM105 <this_file>

try:
    value = int(user_input)
except ValueError:
    pass  # SIM105: use contextlib.suppress()

