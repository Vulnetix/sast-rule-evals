# Sample for Ruff rule PGH003: blanket-type-ignore
# This file is designed to trigger the PGH003 rule.
# Run: ruff check --select PGH003 <this_file>

x: int = value  # type: ignore  # PGH003: use specific codes

