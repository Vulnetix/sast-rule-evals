# Sample for Ruff rule S307: suspicious-eval-usage
# This file is designed to trigger the S307 rule.
# Run: ruff check --select S307 <this_file>

result = eval("1 + 2")  # S307: eval()

