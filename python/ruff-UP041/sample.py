# Sample for Ruff rule UP041: timeout-error-alias
# This file is designed to trigger the UP041 rule.
# Run: ruff check --select UP041 <this_file>

import asyncio

raise asyncio.TimeoutError
