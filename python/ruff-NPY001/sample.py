# Sample for Ruff rule NPY001: numpy-deprecated-type-alias
# This file is designed to trigger the NPY001 rule.
# Run: ruff check --select NPY001 <this_file>

import numpy as np
arr = np.bool(True)  # NPY001: use np.bool_

