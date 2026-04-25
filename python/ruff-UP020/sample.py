# Sample for Ruff rule UP020: open-alias
# This file is designed to trigger the UP020 rule.
# Run: ruff check --select UP020 <this_file>

import io
with io.open("file.txt") as f:  # UP020: use open()
    data = f.read()

