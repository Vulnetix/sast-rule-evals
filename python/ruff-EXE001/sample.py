# Sample for Ruff rule EXE001: shebang-not-executable
# This file is designed to trigger the EXE001 rule.
# Run: ruff check --select EXE001 <this_file>

#!/usr/bin/env python3
# EXE001: has shebang but file not executable
x = 1

