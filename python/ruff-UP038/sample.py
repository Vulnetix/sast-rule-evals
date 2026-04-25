# Sample for Ruff rule UP038: non-pep604-isinstance
def foo(x):
    if isinstance(x, (int, str)):
        return True
    return False
