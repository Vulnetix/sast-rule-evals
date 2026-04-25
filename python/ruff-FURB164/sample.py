# Sample for Ruff rule FURB164: unnecessary-from-float
# This file is designed to trigger the FURB164 rule.
# Run: ruff check --select FURB164 <this_file>

from decimal import Decimal
from fractions import Fraction

Decimal.from_float(4.2)
Decimal.from_float(float("inf"))
Fraction.from_float(4.2)
Fraction.from_decimal(Decimal("4.2"))
