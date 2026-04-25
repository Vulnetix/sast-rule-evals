# Sample for Ruff rule DTZ007: call-datetime-strptime-without-zone
# This file is designed to trigger the DTZ007 rule.
# Run: ruff check --select DTZ007 <this_file>

from datetime import datetime
dt = datetime.strptime("2023-01-01", "%Y-%m-%d")  # DTZ007: naive

