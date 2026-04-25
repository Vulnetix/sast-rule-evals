# Sample for Ruff rule S604: call-with-shell-equals-true
# This file is designed to trigger the S604 rule.
# Run: ruff check --select S604 <this_file>

import os
os.system("ls -la")  # S604

