# Sample for Ruff rule PLW0602: global-variable-not-assigned
# This file is designed to trigger the PLW0602 rule.
# Run: ruff check --select PLW0602 <this_file>

global x  # PLW0602: global var with no assignment in scope
def foo():
    pass

