# Sample for Ruff rule DTZ002: call-datetime-today
# This file is designed to trigger the DTZ002 rule.
# Run: ruff check --select DTZ002 <this_file>

from datetime import datetime
dt = datetime.today()  # DTZ002: no timezone

