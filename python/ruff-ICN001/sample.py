# Sample for Ruff rule ICN001: unconventional-import-alias
# This file is designed to trigger the ICN001 rule.
# Run: ruff check --select ICN001 <this_file>

import numpy  # ICN001: should be 'import numpy as np'
import pandas  # ICN001: should be 'import pandas as pd'

