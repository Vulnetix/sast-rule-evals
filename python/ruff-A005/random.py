# Sample for Ruff rule A005: stdlib-module-shadowing
# This file is named 'random.py', which shadows the Python stdlib module 'random'.
# With strict-checking = true in pyproject.toml, A005 fires even for nested paths.
# Run: ruff check --select A005 random.py

MY_CONSTANT = 42
