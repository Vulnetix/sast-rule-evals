# Sample for Ruff rule S312: suspicious-telnet-usage
# This file is designed to trigger the S312 rule.
# Run: ruff check --select S312 <this_file>

import telnetlib  # S312: telnet

