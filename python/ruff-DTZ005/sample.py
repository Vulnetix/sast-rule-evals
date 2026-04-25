# Sample for Ruff rule DTZ005: call-datetime-now-without-tzinfo
# This file is designed to trigger the DTZ005 rule.
# Run: ruff check --select DTZ005 <this_file>

from datetime import datetime
dt = datetime.now()  # DTZ005: no tz argument

