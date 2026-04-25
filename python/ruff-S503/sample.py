# Sample for Ruff rule S503: ssl-with-bad-defaults
# This file is designed to trigger the S503 rule.
# Run: ruff check --select S503 <this_file>

import ssl


def func(version=ssl.PROTOCOL_TLSv1): ...
