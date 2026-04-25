# Sample for Ruff rule B008: function-call-in-default-argument
# This file is designed to trigger the B008 rule.
# Run: ruff check --select B008 <this_file>

from datetime import datetime

def log_event(timestamp=datetime.now()):  # B008: function call in default
    print(timestamp)

