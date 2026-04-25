# Sample for Ruff rule UP038: non-pep604-isinstance
# This file is designed to trigger the UP038 rule.
# Run: ruff check --select UP038 <this_file>

from typing import Union
if isinstance(x, Union[int, float]):  # UP038: use X | Y
    pass

