# Sample for Ruff rule E201: whitespace-after-open-bracket
# This file is designed to trigger the E201 rule.
# Run: ruff check --select E201 <this_file>

spam( ham[1], {eggs: 2})
spam(ham[ 1], {eggs: 2})
spam(ham[1], { eggs: 2})
