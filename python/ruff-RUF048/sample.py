# Sample for Ruff rule RUF048: map-int-version-parsing
# This file is designed to trigger the RUF048 rule.
# Run: ruff check --select RUF048 <this_file>

import matplotlib  # `__version__ == "3.9.1.post-1"` in our environment

# ValueError: invalid literal for int() with base 10: 'post1'
tuple(map(int, matplotlib.__version__.split(".")))
