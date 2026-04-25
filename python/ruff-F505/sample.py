# Sample for Ruff rule F505: percent-format-missing-argument
# This file is designed to trigger the F505 rule.
# Run: ruff check --select F505 <this_file>

"%(greeting)s, %(name)s" % {"name": "world"}
