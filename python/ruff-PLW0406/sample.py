# Sample for Ruff rule PLW0406: import-self
# This file is designed to trigger the PLW0406 rule.
# Run: ruff check --select PLW0406 <this_file>

import __main__  # PLW0406: module imports itself

