# Sample for Ruff rule UP034: extraneous-parentheses
# This file is designed to trigger the UP034 rule.
# Run: ruff check --select UP034 <this_file>

return (x)  # UP034: extraneous parens

