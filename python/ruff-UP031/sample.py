# Sample for Ruff rule UP031: printf-string-formatting
# This file is designed to trigger the UP031 rule.
# Run: ruff check --select UP031 <this_file>

name = "world"
msg = "Hello %s" % name  # UP031: use format specifiers

