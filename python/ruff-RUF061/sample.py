# Sample for Ruff rule RUF061: legacy-form-pytest-raises
# This file is designed to trigger the RUF061 rule.
# Run: ruff check --select RUF061 <this_file>

import pytest


excinfo = pytest.raises(ValueError, int, "hello")
pytest.warns(UserWarning, my_function, arg)
pytest.deprecated_call(my_deprecated_function, arg1, arg2)
