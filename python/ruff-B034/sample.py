# Sample for Ruff rule B034: re-sub-positional-args
# This file is designed to trigger the B034 rule.
# Run: ruff check --select B034 <this_file>

import re

re.split("pattern", "replacement", 1)
