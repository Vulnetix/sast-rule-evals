# Sample for Ruff rule PD011: pandas-use-of-dot-values
# This file is designed to trigger the PD011 rule.
# Run: ruff check --select PD011 <this_file>

import pandas as pd
df = pd.DataFrame({"a": [1, 2]})
arr = df.values  # PD011: use .to_numpy()

