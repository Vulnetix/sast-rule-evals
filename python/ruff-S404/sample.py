# Sample for Ruff rule S404: suspicious-subprocess-import
# This file is designed to trigger the S404 rule.
# Run: ruff check --select S404 <this_file>

import subprocess  # S404

