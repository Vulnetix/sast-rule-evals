# Sample for Ruff rule PLR1711: useless-return
# This file is designed to trigger the PLR1711 rule.
# Run: ruff check --select PLR1711 <this_file>

def nothing():
    pass
    return None  # PLR1711: useless return None

