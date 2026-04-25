# Sample for Ruff rule DTZ003: call-datetime-utcnow
# This file is designed to trigger the DTZ003 rule.
# Run: ruff check --select DTZ003 <this_file>

from datetime import datetime
dt = datetime.utcnow()  # DTZ003: naive datetime

