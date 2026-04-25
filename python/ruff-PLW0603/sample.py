# Sample for Ruff rule PLW0603: global-statement
# This file is designed to trigger the PLW0603 rule.
# Run: ruff check --select PLW0603 <this_file>

global counter  # PLW0603: using global
counter = 0

