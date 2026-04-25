# Sample for Ruff rule SIM115: open-file-with-context-handler
# This file is designed to trigger the SIM115 rule.
# Run: ruff check --select SIM115 <this_file>

f = open("data.txt")  # SIM115: use context manager
data = f.read()
f.close()

