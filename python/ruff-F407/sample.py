# Sample for Ruff rule F407: future-feature-not-defined
# This file is designed to trigger the F407 rule.
# Run: ruff check --select F407 <this_file>

from __future__ import nonexistent_feature  # F407: not a valid future feature
