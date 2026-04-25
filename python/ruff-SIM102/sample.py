# Sample for Ruff rule SIM102: collapsible-if
# This file is designed to trigger the SIM102 rule.
# Run: ruff check --select SIM102 <this_file>

if foo:
    if bar:
        ...
