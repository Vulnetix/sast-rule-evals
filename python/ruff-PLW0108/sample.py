# Sample for Ruff rule PLW0108: unnecessary-lambda
# This file is designed to trigger the PLW0108 rule.
# Run: ruff check --select PLW0108 <this_file>

df.apply(lambda x: str(x))
