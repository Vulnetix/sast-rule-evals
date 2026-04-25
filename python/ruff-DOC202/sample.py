# Sample for Ruff rule DOC202: docstring-extraneous-returns
# This file is designed to trigger the DOC202 rule.
# Run: ruff check --select DOC202 <this_file>

def say_hello(n: int) -> None:
    """Says hello to the user.

    Args:
        n: Number of times to say hello.

    Returns:
        Doesn't return anything.
    """
    for _ in range(n):
        print("Hello!")
