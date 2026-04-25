# Sample for Ruff rule DOC403: docstring-extraneous-yields
# This file is designed to trigger the DOC403 rule.
# Run: ruff check --select DOC403 <this_file>

def say_hello(n: int) -> None:
    """Says hello to the user.

    Args:
        n: Number of times to say hello.

    Yields:
        Doesn't yield anything.
    """
    for _ in range(n):
        print("Hello!")
