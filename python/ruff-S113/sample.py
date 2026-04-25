# Sample for Ruff rule S113: request-without-timeout
# This file is designed to trigger the S113 rule.
# Run: ruff check --select S113 <this_file>

import requests
r = requests.get("https://example.com")  # S113: no timeout

