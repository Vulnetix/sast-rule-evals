# Sample for Ruff rule PLE0643: potential-index-error
# This file is designed to trigger the PLE0643 rule.
# Run: ruff check --select PLE0643 <this_file>

print([0, 1, 2][3])
