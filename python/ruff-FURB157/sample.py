# Sample for Ruff rule FURB157: verbose-decimal-constructor
# This file is designed to trigger the FURB157 rule.
# Run: ruff check --select FURB157 <this_file>

from decimal import Decimal
d = Decimal("10")  # FURB157: use Decimal(10) directly

