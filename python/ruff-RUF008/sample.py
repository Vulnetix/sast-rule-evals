# Sample for Ruff rule RUF008: mutable-dataclass-default
# This file is designed to trigger the RUF008 rule.
# Run: ruff check --select RUF008 <this_file>

from dataclasses import dataclass


@dataclass
class A:
    # A list without a `default_factory` or `ClassVar` annotation
    # will raise a `ValueError`.
    mutable_default: list[int] = []
