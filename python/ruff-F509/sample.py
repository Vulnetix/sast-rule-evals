# Sample for Ruff rule F509: percent-format-unsupported-format-character
# This file is designed to trigger the F509 rule.
# Run: ruff check --select F509 <this_file>

"Hello, %S" % "world"
