# Sample for Ruff rule SIM107: return-in-try-except-finally
# This file is designed to trigger the SIM107 rule.
# Run: ruff check --select SIM107 <this_file>

def squared(n):
    try:
        sqr = n**2
        return sqr
    except Exception:
        return "An exception occurred"
    finally:
        return -1  # Always returns -1.
