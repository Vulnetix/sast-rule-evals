# Sample for Ruff rule PLW0129: assert-on-string-literal
# This file is designed to trigger the PLW0129 rule.
# Run: ruff check --select PLW0129 <this_file>

assert (x > 0, "x must be positive")  # PLW0129: assert tuple always True

