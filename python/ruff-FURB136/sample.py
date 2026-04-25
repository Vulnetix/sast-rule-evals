# Sample for Ruff rule FURB136: if-expr-min-max
# This file is designed to trigger the FURB136 rule.
# Run: ruff check --select FURB136 <this_file>

score1, score2 = 4, 5

highest_score = score1 if score1 > score2 else score2
