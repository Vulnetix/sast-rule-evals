# Sample for Ruff rule F811: redefined-while-unused
# This file is designed to trigger the F811 rule.
# Run: ruff check --select F811 <this_file>

import foo
import bar
import foo  # Redefinition of unused `foo` from line 1
