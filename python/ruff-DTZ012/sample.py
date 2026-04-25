# Sample for Ruff rule DTZ012: call-date-fromtimestamp
# This file is designed to trigger the DTZ012 rule.
# Run: ruff check --select DTZ012 <this_file>

import datetime

datetime.date.fromtimestamp(946684800)
