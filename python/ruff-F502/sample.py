# Sample for Ruff rule F502: percent-format-expected-mapping
# This file is designed to trigger the F502 rule.
# Run: ruff check --select F502 <this_file>

"%(greeting)s, %(name)s" % ("Hello", "World")
