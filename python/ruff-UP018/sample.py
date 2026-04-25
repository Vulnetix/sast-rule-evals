# Sample for Ruff rule UP018: native-literals
# This file is designed to trigger the UP018 rule.
# Run: ruff check --select UP018 <this_file>

x = int(42)  # UP018: unnecessary int()
s = str("hello")

