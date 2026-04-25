# Sample for Ruff rule PLC2701: import-private-name
# This file is designed to trigger the PLC2701 rule.
# Run: ruff check --select PLC2701 <this_file>

from foo import _bar
