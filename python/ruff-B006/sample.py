# Sample for Ruff rule B006: mutable-argument-default
# This file is designed to trigger the B006 rule.
# Run: ruff check --select B006 <this_file>

def process(items=[]):  # B006: mutable default
    items.append(1)
    return items

