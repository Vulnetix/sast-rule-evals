# Sample for Ruff rule FURB177: implicit-cwd
# This file is designed to trigger the FURB177 rule.
# Run: ruff check --select FURB177 <this_file>

from pathlib import Path
cwd = Path(".")  # FURB177: use Path.cwd()

