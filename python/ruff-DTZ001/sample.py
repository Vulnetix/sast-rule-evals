# Sample for Ruff rule DTZ001: call-datetime-without-tzinfo
# This file is designed to trigger the DTZ001 rule.
# Run: ruff check --select DTZ001 <this_file>

from datetime import datetime
dt = datetime(2023, 1, 1)  # DTZ001: no tzinfo

