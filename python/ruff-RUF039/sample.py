# Sample for Ruff rule RUF039: unraw-re-pattern
# This file is designed to trigger the RUF039 rule.
# Run: ruff check --select RUF039 <this_file>

# Literal is `1\n2`.
re.compile("1\n2")

# Literal is `1\\n2`, but the regex library will interpret `\\n` and will still match a newline
# character as before.
re.compile(r"1\n2")
