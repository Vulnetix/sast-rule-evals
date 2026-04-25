# Sample for Ruff rule FURB167: regex-flag-alias
# This file is designed to trigger the FURB167 rule.
# Run: ruff check --select FURB167 <this_file>

import re
pattern = re.compile("foo", re.IGNORECASE)  # FURB167: use re.I flag literal

