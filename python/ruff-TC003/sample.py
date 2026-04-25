# Sample for Ruff rule TC003: typing-only-standard-library-import
# This file is designed to trigger the TC003 rule.
# Run: ruff check --select TC003 <this_file>

from __future__ import annotations

from pathlib import Path


def func(path: Path) -> str:
    return str(path)
