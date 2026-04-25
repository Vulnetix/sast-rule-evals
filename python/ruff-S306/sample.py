# Sample for Ruff rule S306: suspicious-mktemp-usage
# This file is designed to trigger the S306 rule.
# Run: ruff check --select S306 <this_file>

import tempfile

tmp_file = tempfile.mktemp()
with open(tmp_file, "w") as file:
    file.write("Hello, world!")
