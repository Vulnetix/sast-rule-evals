# Sample for Ruff rule PD901: pandas-df-variable-name
# This file is designed to trigger the PD901 rule.
# Run: ruff check --select PD901 <this_file>

import pandas as pd

df = pd.read_csv("animals.csv")
