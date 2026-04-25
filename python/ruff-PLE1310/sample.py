# Sample for Ruff rule PLE1310: bad-str-strip-call
# This file is designed to trigger the PLE1310 rule.
# Run: ruff check --select PLE1310 <this_file>

s = "hello"
stripped = s.strip("abc")  # PLE1310: strip with multi-char

