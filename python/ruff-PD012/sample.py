# Sample for Ruff rule PD012: pandas-use-of-dot-read-table
# This file is designed to trigger the PD012 rule.
# Run: ruff check --select PD012 <this_file>

import pandas as pd

cities_df = pd.read_table("cities.csv", sep=",")
