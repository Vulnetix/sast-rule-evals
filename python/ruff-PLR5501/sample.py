# Sample for Ruff rule PLR5501: collapsible-else-if
# This file is designed to trigger the PLR5501 rule.
# Run: ruff check --select PLR5501 <this_file>

def check(x):
    if x > 0:
        return "pos"
    else:
        if x < 0:  # PLR5501: use elif
            return "neg"

