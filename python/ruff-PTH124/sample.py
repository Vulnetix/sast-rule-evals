# Sample for Ruff rule PTH124: py-path
# This file is designed to trigger the PTH124 rule.
# Run: ruff check --select PTH124 <this_file>

import py.path

p = py.path.local("/foo/bar").join("baz/qux")
