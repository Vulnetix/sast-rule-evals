# Sample for Ruff rule PD010: pandas-use-of-dot-pivot-or-unstack
# This file is designed to trigger the PD010 rule.
# Run: ruff check --select PD010 <this_file>

import pandas as pd

df = pd.read_csv("cities.csv")
df.pivot(index="city", columns="year", values="population")
