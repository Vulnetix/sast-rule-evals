# Sample for Ruff rule RUF065: logging-eager-conversion
# This file is designed to trigger the RUF065 rule.
# Run: ruff check --select RUF065 <this_file>

import logging

logging.basicConfig(format="%(message)s", level=logging.INFO)

user = "Maria"

logging.info("%s - Something happened", str(user))
