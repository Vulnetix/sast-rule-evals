# Sample for Ruff rule UP045: non-pep604-annotation-optional
# This file is designed to trigger the UP045 rule.
# Run: ruff check --select UP045 <this_file>

from typing import Optional

foo: Optional[int] = None
