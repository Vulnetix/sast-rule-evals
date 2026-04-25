# Sample for Ruff rule T203: p-print
# This file is designed to trigger the T203 rule.
# Run: ruff check --select T203 <this_file>

from pprint import pprint
pprint({"key": "value"})  # T203

