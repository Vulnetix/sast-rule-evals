# Sample for Ruff rule B028: no-explicit-stacklevel
# This file is designed to trigger the B028 rule.
# Run: ruff check --select B028 <this_file>

import warnings
warnings.warn("deprecated function, use new_function instead")  # B028: no level
