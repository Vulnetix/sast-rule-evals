# Sample for Ruff rule PLC0414: useless-import-alias
# This file is designed to trigger the PLC0414 rule.
# Run: ruff check --select PLC0414 <this_file>

import os as os  # PLC0414: alias same as name

