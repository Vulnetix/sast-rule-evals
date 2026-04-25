# Sample for Ruff rule DTZ011: call-date-today
# This file is designed to trigger the DTZ011 rule.
# Run: ruff check --select DTZ011 <this_file>

from datetime import date
d = date.today()  # DTZ011: no timezone

