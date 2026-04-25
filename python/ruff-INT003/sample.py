# Sample for Ruff rule INT003: printf-in-get-text-func-call
# This file is designed to trigger the INT003 rule.
# Run: ruff check --select INT003 <this_file>

from gettext import gettext as _

name = "Maria"
_("Hello, %s!" % name)  # Looks for "Hello, Maria!".
