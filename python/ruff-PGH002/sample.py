# Sample for Ruff rule PGH002: deprecated-log-warn
# This file is designed to trigger the PGH002 rule.
# Run: ruff check --select PGH002 <this_file>

import warnings
warnings.warn("use new_func", DeprecationWarning)  # PGH002: deprecated

