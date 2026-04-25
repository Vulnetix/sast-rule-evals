# Sample for Ruff rule A005: stdlib-module-shadowing
# A005 fires based on the MODULE FILENAME, not file content.
# The rule triggers when a file is named the same as a Python stdlib module.
# See 'random.py' in this directory - that file's name triggers A005.
# Run: ruff check --select A005 random.py
