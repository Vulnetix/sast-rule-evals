# Sample for Ruff rule PLW0604: global-at-module-level
# This file is designed to trigger the PLW0604 rule.
# Run: ruff check --select PLW0604 <this_file>

counter = 0

def increment():
    global counter  # PLW0604: assigned at module level
    counter += 1

