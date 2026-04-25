# Sample for Ruff rule PD013: pandas-use-of-dot-stack
# This file is designed to trigger the PD013 rule.
# Run: ruff check --select PD013 <this_file>

import pandas as pd

cities_df = pd.read_csv("cities.csv")
cities_df.set_index("city").stack()
