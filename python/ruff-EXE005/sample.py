# Sample for Ruff rule EXE005: shebang-not-first-line
# This file is designed to trigger the EXE005 rule.
# Run: ruff check --select EXE005 <this_file>

foo = 1
#!/usr/bin/env python3
