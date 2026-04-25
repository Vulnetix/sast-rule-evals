# Sample for Ruff rule PLR1704: redefined-argument-from-local
# This file is designed to trigger the PLR1704 rule.
# Run: ruff check --select PLR1704 <this_file>

def show(host_id=10.11):
    for host_id, host in [[12.13, "Venus"], [14.15, "Mars"]]:
        print(host_id, host)
