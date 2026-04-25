# Sample for Ruff rule PLW1501: bad-open-mode
# This file is designed to trigger the PLW1501 rule.
# Run: ruff check --select PLW1501 <this_file>

with open("file", "rwx") as f:
    content = f.read()
