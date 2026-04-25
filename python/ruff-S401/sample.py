# Sample for Ruff rule S401: suspicious-telnetlib-import
# This file is designed to trigger the S401 rule.
# Run: ruff check --select S401 <this_file>

import telnetlib  # S401

