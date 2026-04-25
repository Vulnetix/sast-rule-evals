# Sample for Ruff rule DTZ004: call-datetime-utcfromtimestamp
# This file is designed to trigger the DTZ004 rule.
# Run: ruff check --select DTZ004 <this_file>

from datetime import datetime
dt = datetime.utcfromtimestamp(0)  # DTZ004: naive

