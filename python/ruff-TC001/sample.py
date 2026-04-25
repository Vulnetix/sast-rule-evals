# Sample for Ruff rule TC001: typing-only-first-party-import
# This file is designed to trigger the TC001 rule.
# Run: ruff check --select TC001 <this_file>

from typing import TYPE_CHECKING
import os  # TC001: should be in TYPE_CHECKING block

