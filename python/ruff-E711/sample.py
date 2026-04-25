# Sample for Ruff rule E711: none-comparison
# This file is designed to trigger the E711 rule.
# Run: ruff check --select E711 <this_file>

x = None
if x == None:  # E711: comparison to None
    pass
if None == x:  # E711: yoda
    pass

