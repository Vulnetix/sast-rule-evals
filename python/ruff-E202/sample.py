# Sample for Ruff rule E202: whitespace-before-close-bracket
# This file is designed to trigger the E202 rule.
# Run: ruff check --select E202 <this_file>

spam(ham[1], {eggs: 2} )
spam(ham[1 ], {eggs: 2})
spam(ham[1], {eggs: 2 })
