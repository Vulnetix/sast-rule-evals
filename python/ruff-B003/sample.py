# Sample for Ruff rule B003: assignment-to-os-environ
# This file is designed to trigger the B003 rule.
# Run: ruff check --select B003 <this_file>

import os
debug = os.environ["DEBUG"]  # B003: prefer os.getenv

