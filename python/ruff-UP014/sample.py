# Sample for Ruff rule UP014: convert-named-tuple-functional-to-class
# This file is designed to trigger the UP014 rule.
# Run: ruff check --select UP014 <this_file>

from typing import NamedTuple
Point = NamedTuple("Point", [("x", float), ("y", float)])  # UP014: use class syntax

