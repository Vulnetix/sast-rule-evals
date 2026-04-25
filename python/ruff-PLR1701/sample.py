# Sample for Ruff rule PLR1701: repeated-isinstance-calls
def check(x):
    if isinstance(x, int) or isinstance(x, str):
        return True
    return False
