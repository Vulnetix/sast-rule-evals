# Sample for Ruff rule UP032: f-string
# This file is designed to trigger the UP032 rule.
# Run: ruff check --select UP032 <this_file>

name = "world"
msg = "Hello {}".format(name)  # UP032: use f-string

