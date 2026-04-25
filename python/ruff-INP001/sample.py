# Sample for Ruff rule INP001: implicit-namespace-package
# This file is designed to trigger the INP001 rule.
# Run: ruff check --select INP001 <this_file>

# This file has no __init__.py in parent, making it implicit namespace package
x = 1

