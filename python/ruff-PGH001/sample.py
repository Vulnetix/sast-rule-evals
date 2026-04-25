# Sample for Ruff rule PGH001: eval
# This file is designed to trigger the PGH001 rule.
# Run: ruff check --select PGH001 <this_file>

result = eval(user_input)  # PGH001: no eval

