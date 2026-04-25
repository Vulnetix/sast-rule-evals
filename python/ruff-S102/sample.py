# Sample for Ruff rule S102: exec-builtin
# This file is designed to trigger the S102 rule.
# Run: ruff check --select S102 <this_file>

exec("print('hello')")  # S102: exec()

