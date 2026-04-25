# Sample for Ruff rule PD004: pandas-use-of-dot-not-null
# This file is designed to trigger the PD004 rule.
# Run: ruff check --select PD004 <this_file>

import pandas as pd

animals_df = pd.read_csv("animals.csv")
pd.notnull(animals_df)
