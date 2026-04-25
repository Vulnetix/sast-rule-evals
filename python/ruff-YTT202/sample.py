# Sample for Ruff rule YTT202: six-py3
# This file is designed to trigger the YTT202 rule.
# Run: ruff check --select YTT202 <this_file>

import six

six.PY3  # `False` on Python 4.
