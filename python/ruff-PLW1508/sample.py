# Sample for Ruff rule PLW1508: invalid-envvar-default
# This file is designed to trigger the PLW1508 rule.
# Run: ruff check --select PLW1508 <this_file>

import os
port = os.getenv("PORT", 8080)  # PLW1508: wrong type default (int not str)

