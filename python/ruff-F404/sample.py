# Sample for Ruff rule F404: late-future-import
# This file is designed to trigger the F404 rule.
# Run: ruff check --select F404 <this_file>

from pathlib import Path

from __future__ import annotations
