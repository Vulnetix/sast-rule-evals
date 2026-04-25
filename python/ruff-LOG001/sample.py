# Sample for Ruff rule LOG001: direct-logger-instantiation
# This file is designed to trigger the LOG001 rule.
# Run: ruff check --select LOG001 <this_file>

import logging

logger = logging.Logger(__name__)
