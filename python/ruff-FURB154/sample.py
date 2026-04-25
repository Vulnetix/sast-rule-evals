# Sample for Ruff rule FURB154: repeated-global
# This file is designed to trigger the FURB154 rule.
# Run: ruff check --select FURB154 <this_file>

def func():
    global x
    global y

    print(x, y)
