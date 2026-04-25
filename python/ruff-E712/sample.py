# Sample for Ruff rule E712: true-false-comparison
# This file is designed to trigger the E712 rule.
# Run: ruff check --select E712 <this_file>

flag = True
if flag == True:  # E712: comparison to True
    pass
if flag == False:  # E712
    pass

