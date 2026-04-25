# Sample for Ruff rule PLE0116: continue-in-finally
# This file is designed to trigger the PLE0116 rule.
# Run: ruff check --select PLE0116 <this_file>

while True:
    try:
        pass
    finally:
        continue
