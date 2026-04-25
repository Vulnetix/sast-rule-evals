# Sample for Ruff rule FURB152: math-constant
# This file is designed to trigger the FURB152 rule.
# Run: ruff check --select FURB152 <this_file>

import math
tau = math.pi * 2  # FURB152: use math.tau

