# Sample for Ruff rule PTH208: os-listdir
# This file is designed to trigger the PTH208 rule.
# Run: ruff check --select PTH208 <this_file>

p = "."
for d in os.listdir(p):
    ...

if os.listdir(p):
    ...

if "file" in os.listdir(p):
    ...
