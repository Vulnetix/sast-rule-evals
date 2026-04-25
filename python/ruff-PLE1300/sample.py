# Sample for Ruff rule PLE1300: bad-string-format-character
# This file is designed to trigger the PLE1300 rule.
# Run: ruff check --select PLE1300 <this_file>

# `z` is not a valid format type.
print("%z" % "1")

print("{:z}".format("1"))
