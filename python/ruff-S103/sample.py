# Sample for Ruff rule S103: bad-file-permissions
# This file is designed to trigger the S103 rule.
# Run: ruff check --select S103 <this_file>

import os

os.chmod("/etc/secrets.txt", 0o666)  # rw-rw-rw-
