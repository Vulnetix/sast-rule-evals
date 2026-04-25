# Sample for Ruff rule TC006: runtime-cast-value
# This file is designed to trigger the TC006 rule.
# Run: ruff check --select TC006 <this_file>

from typing import cast

x = cast(dict[str, int], foo)
