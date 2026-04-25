# Sample for Ruff rule FURB163: redundant-log-base
# This file is designed to trigger the FURB163 rule.
# Run: ruff check --select FURB163 <this_file>

import math
log2 = math.log(x, 2)  # FURB163: use math.log2

