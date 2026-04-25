# Sample for Ruff rule PTH210: invalid-pathlib-with-suffix
# This file is designed to trigger the PTH210 rule.
# Run: ruff check --select PTH210 <this_file>

from pathlib import Path

path = Path()

path.with_suffix("py")
