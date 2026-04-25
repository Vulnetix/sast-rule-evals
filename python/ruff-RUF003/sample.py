# Sample for Ruff rule RUF003: ambiguous-unicode-character-comment
# This file is designed to trigger the RUF003 rule.
# Run: ruff check --select RUF003 <this_file>

foo()  # nоqa  # "о" is Cyrillic (`U+043E`)
