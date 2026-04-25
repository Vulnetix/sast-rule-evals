# Sample for Ruff rule S108: hardcoded-temp-file
# This file is designed to trigger the S108 rule.
# Run: ruff check --select S108 <this_file>

import tempfile
tmp = "/tmp/myfile"  # S108: insecure temp path

