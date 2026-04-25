# Sample for Ruff rule G101: logging-extra-attr-clash
# This file is designed to trigger the G101 rule.
# Run: ruff check --select G101 <this_file>

import logging

logging.basicConfig(format="%(name) - %(message)s", level=logging.INFO)

username = "Maria"

logging.info("Something happened", extra=dict(name=username))
