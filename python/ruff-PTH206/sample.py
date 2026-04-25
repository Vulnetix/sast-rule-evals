# Sample for Ruff rule PTH206: os-sep-split
# This file is designed to trigger the PTH206 rule.
# Run: ruff check --select PTH206 <this_file>

import os

"path/to/file_name.txt".split(os.sep)[-1]

"path/to/file_name.txt".split(os.sep)[-2]

# Iterating over the path parts
if any(part in blocklist for part in "my/file/path".split(os.sep)):
    ...
