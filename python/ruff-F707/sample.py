# Sample for Ruff rule F707: default-except-not-last
# This file is designed to trigger the F707 rule.
# Run: ruff check --select F707 <this_file>

def reciprocal(n):
    try:
        reciprocal = 1 / n
    except:
        print("An exception occurred.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        return reciprocal
