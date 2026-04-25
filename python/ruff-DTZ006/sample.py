# Sample for Ruff rule DTZ006: call-datetime-fromtimestamp
# This file is designed to trigger the DTZ006 rule.
# Run: ruff check --select DTZ006 <this_file>

from datetime import datetime
dt = datetime.fromtimestamp(timestamp)  # DTZ006: no tz

