# Sample for Ruff rule UP017: datetime-timezone-utc
# This file is designed to trigger the UP017 rule.
# Run: ruff check --select UP017 <this_file>

import datetime

datetime.timezone.utc
