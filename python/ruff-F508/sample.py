# Sample for Ruff rule F508: percent-format-star-requires-sequence
# This file is designed to trigger the F508 rule.
# Run: ruff check --select F508 <this_file>

from math import pi

"%(n).*f" % {"n": (2, pi)}
