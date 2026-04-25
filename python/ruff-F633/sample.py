# Sample for Ruff rule F633: invalid-print-syntax
# This file is designed to trigger the F633 rule.
# Run: ruff check --select F633 <this_file>

from __future__ import print_function
import sys

print >> sys.stderr, "Hello, world!"
