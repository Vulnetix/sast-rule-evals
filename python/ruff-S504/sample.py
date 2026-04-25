# Sample for Ruff rule S504: ssl-with-no-version
# This file is designed to trigger the S504 rule.
# Run: ruff check --select S504 <this_file>

import ssl

ssl.wrap_socket()
