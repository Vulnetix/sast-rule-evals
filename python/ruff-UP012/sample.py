# Sample for Ruff rule UP012: unnecessary-encode-utf8
# This file is designed to trigger the UP012 rule.
# Run: ruff check --select UP012 <this_file>

data = "hello".encode("utf-8")  # UP012: unnecessary encode

