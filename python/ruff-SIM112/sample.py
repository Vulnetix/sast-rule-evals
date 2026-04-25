# Sample for Ruff rule SIM112: uncapitalized-environment-variables
# This file is designed to trigger the SIM112 rule.
# Run: ruff check --select SIM112 <this_file>

import os
val = os.environ.get("my_var")  # SIM112: use uppercase

