# Sample for Ruff rule B022: useless-contextlib-suppress
# This file is designed to trigger the B022 rule.
# Run: ruff check --select B022 <this_file>

import contextlib
with contextlib.suppress():  # B022: no args
    pass

