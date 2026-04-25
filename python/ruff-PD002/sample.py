# Sample for Ruff rule PD002: pandas-use-of-inplace-argument
# This file is designed to trigger the PD002 rule.
# Run: ruff check --select PD002 <this_file>

import pandas as pd
df = pd.DataFrame({"a": [1, 2]})
df.drop_duplicates(inplace=True)  # PD002: use assignment

