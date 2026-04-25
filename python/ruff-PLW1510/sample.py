# Sample for Ruff rule PLW1510: subprocess-run-without-check
# This file is designed to trigger the PLW1510 rule.
# Run: ruff check --select PLW1510 <this_file>

import subprocess

subprocess.run(["ls", "nonexistent"])  # No exception raised.
