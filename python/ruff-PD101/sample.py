# Sample for Ruff rule PD101: pandas-nunique-constant-series-check
# This file is designed to trigger the PD101 rule.
# Run: ruff check --select PD101 <this_file>

import pandas as pd

data = pd.Series(range(1000))
if data.nunique() <= 1:
    print("Series is constant")
