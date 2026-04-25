# Sample for Ruff rule S603: subprocess-without-shell-equals-true
# This file is designed to trigger the S603 rule.
# Run: ruff check --select S603 <this_file>

import subprocess
result = subprocess.call(["ls", "-la"])  # S603

