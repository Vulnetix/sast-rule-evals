# Sample for Ruff rule DTZ901: datetime-min-max
# This file is designed to trigger the DTZ901 rule.
# Run: ruff check --select DTZ901 <this_file>

import datetime

# Timezone: UTC-14
datetime.datetime.min.timestamp()  # ValueError: year 0 is out of range
datetime.datetime.max.timestamp()  # ValueError: year 10000 is out of range
