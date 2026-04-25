# Sample for Ruff rule PD003: pandas-use-of-dot-is-null
# This file is designed to trigger the PD003 rule.
# Run: ruff check --select PD003 <this_file>

import pandas as pd
df = pd.DataFrame()
mask = df["col"].isnull()  # PD003: use .isna()

