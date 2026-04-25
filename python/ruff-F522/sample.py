# Sample for Ruff rule F522: string-dot-format-extra-named-arguments
# This file is designed to trigger the F522 rule.
# Run: ruff check --select F522 <this_file>

"Hello, {name}".format(greeting="Hello", name="World")
