# Sample for Ruff rule RUF028: invalid-formatter-suppression-comment
# This file is designed to trigger the RUF028 rule.
# Run: ruff check --select RUF028 <this_file>

def decorator():
    pass


@decorator
# fmt: off
def example():
    if True:
        # fmt: skip
        expression = [
            # fmt: off
            1,
            2,
        ]
        # yapf: disable
    # fmt: on
    # yapf: enable
