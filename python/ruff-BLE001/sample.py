# Sample for Ruff rule BLE001: blind-except
# This file is designed to trigger the BLE001 rule.
# Run: ruff check --select BLE001 <this_file>

try:
    risky()
except BaseException:  # BLE001: too broad
    pass

