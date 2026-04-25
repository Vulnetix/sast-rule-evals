# Sample for Ruff rule S502: ssl-insecure-version
# This file is designed to trigger the S502 rule.
# Run: ruff check --select S502 <this_file>

import ssl

ssl.wrap_socket(ssl_version=ssl.PROTOCOL_TLSv1)
