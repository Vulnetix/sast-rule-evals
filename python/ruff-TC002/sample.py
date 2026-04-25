# Sample for Ruff rule TC002: typing-only-third-party-import
# This file is designed to trigger the TC002 rule.
# Run: ruff check --select TC002 <this_file>

from __future__ import annotations

import pandas as pd


def func(df: pd.DataFrame) -> int:
    return len(df)
