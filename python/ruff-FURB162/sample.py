# Sample for Ruff rule FURB162: fromisoformat-replace-z
# This file is designed to trigger the FURB162 rule.
# Run: ruff check --select FURB162 <this_file>

from datetime import datetime


date = "2025-01-01T00:00:00Z"

datetime.fromisoformat(date.replace("Z", "+00:00"))
datetime.fromisoformat(date[:-1] + "-00")
datetime.fromisoformat(date.strip("Z", "-0000"))
datetime.fromisoformat(date.rstrip("Z", "-00:00"))
