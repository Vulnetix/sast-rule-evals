# Sample for Ruff rule RUF009: function-call-in-dataclass-default-argument
# This file is designed to trigger the RUF009 rule.
# Run: ruff check --select RUF009 <this_file>

from dataclasses import dataclass

@dataclass
class Config:
    items: list = list()  # RUF009: mutable default in dataclass

