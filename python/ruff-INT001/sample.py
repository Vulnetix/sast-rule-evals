# Sample for Ruff rule INT001: f-string-in-get-text-func-call
# This file is designed to trigger the INT001 rule.
# Run: ruff check --select INT001 <this_file>

from gettext import gettext as _
msg = _(f"Hello {name}")  # INT001: f-string in gettext

