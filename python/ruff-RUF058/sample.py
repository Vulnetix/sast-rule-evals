# Sample for Ruff rule RUF058: starmap-zip
# This file is designed to trigger the RUF058 rule.
# Run: ruff check --select RUF058 <this_file>

from itertools import starmap


starmap(func, zip(a, b))
starmap(func, zip(a, b, strict=True))
