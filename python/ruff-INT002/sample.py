# Sample for Ruff rule INT002: format-in-get-text-func-call
# This file is designed to trigger the INT002 rule.
# Run: ruff check --select INT002 <this_file>

from gettext import gettext as _

name = "Maria"
_("Hello, {}!".format(name))  # Looks for "Hello, Maria!".
