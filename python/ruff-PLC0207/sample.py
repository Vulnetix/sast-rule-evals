# Sample for Ruff rule PLC0207: missing-maxsplit-arg
# This file is designed to trigger the PLC0207 rule.
# Run: ruff check --select PLC0207 <this_file>

url = "www.example.com"
prefix = url.split(".")[0]
