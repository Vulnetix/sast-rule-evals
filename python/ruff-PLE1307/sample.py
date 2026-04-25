# Sample for Ruff rule PLE1307: bad-string-format-type
# This file is designed to trigger the PLE1307 rule.
# Run: ruff check --select PLE1307 <this_file>

print("%d" % "1")
