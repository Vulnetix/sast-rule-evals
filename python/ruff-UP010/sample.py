# Sample for Ruff rule UP010: unnecessary-future-import
# This file is designed to trigger the UP010 rule.
# Run: ruff check --select UP010 <this_file>

from __future__ import print_function

print("Hello, world!")
