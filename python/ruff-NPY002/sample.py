# Sample for Ruff rule NPY002: numpy-legacy-random
# This file is designed to trigger the NPY002 rule.
# Run: ruff check --select NPY002 <this_file>

import numpy as np
rng = np.random.randint(0, 10)  # NPY002: use Generator

