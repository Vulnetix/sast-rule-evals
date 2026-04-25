# Sample for Ruff rule FA102: future-required-type-annotation
# This file is designed to trigger the FA102 rule.
# Run: ruff check --select FA102 <this_file>

def func(obj: dict[str, int | None]) -> None: ...
