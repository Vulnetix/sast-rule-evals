# Sample for Ruff rule NPY003: numpy-deprecated-function
# This file is designed to trigger the NPY003 rule.
# Run: ruff check --select NPY003 <this_file>

import numpy as np

np.alltrue([True, False])
