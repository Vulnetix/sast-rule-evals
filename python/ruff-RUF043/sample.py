# Sample for Ruff rule RUF043: pytest-raises-ambiguous-pattern
# This file is designed to trigger the RUF043 rule.
# Run: ruff check --select RUF043 <this_file>

import pytest


with pytest.raises(Exception, match="A full sentence."):
    do_thing_that_raises()
