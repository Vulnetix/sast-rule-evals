# Sample for Ruff rule F506: percent-format-mixed-positional-and-named
# This file is designed to trigger the F506 rule.
# Run: ruff check --select F506 <this_file>

"%s, %(name)s" % ("Hello", {"name": "World"})
