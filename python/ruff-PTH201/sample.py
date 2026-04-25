# Sample for Ruff rule PTH201: path-constructor-current-directory
# This file is designed to trigger the PTH201 rule.
# Run: ruff check --select PTH201 <this_file>

from pathlib import Path

_ = Path(".")
