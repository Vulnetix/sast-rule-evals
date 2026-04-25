# Sample for Ruff rule PLE1206: logging-too-few-args
# This file is designed to trigger the PLE1206 rule.
# Run: ruff check --select PLE1206 <this_file>

import logging

try:
    function()
except Exception as e:
    logging.error("%s error occurred: %s", e)
    raise
