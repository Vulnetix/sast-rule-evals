# Sample for Ruff rule S606: start-process-with-no-shell
# This file is designed to trigger the S606 rule.
# Run: ruff check --select S606 <this_file>

import os
os.system("ls")  # S606

