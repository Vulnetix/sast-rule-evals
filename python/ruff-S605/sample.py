# Sample for Ruff rule S605: start-process-with-a-shell
# This file is designed to trigger the S605 rule.
# Run: ruff check --select S605 <this_file>

import os
os.system("echo " + user_input)  # S605: injection risk

