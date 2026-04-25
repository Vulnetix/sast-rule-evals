# Sample for Ruff rule A006: builtin-lambda-argument-shadowing
# This file is designed to trigger the A006 rule.
# Run: ruff check --select A006 <this_file>

# Lambda argument 'list' shadows the builtin 'list'
f = lambda list: list[0]  # noqa: E731 - intentional for testing A006

# Lambda argument 'len' shadows the builtin 'len'
g = lambda len: len + 1  # noqa: E731

# Lambda argument 'type' shadows the builtin 'type'
h = lambda type, x: type(x)  # noqa: E731
