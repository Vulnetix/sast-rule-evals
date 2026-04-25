# Sample for Ruff rule UP025: unicode-kind-prefix
# This file is designed to trigger the UP025 rule.
# Run: ruff check --select UP025 <this_file>

msg = u"hello"  # UP025: unicode literal unnecessary in py3

