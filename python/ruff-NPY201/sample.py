# Sample for Ruff rule NPY201: numpy2-deprecation
# This file is designed to trigger the NPY201 rule.
# Run: ruff check --select NPY201 <this_file>

import numpy as np

arr1 = [np.Infinity, np.NaN, np.nan, np.PINF, np.inf]
arr2 = [np.float_(1.5), np.float64(5.1)]
np.round_(arr2)
