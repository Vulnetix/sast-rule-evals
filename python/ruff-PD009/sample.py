# Sample for Ruff rule PD009: pandas-use-of-dot-iat
# This file is designed to trigger the PD009 rule.
# Run: ruff check --select PD009 <this_file>

import pandas as pd

students_df = pd.read_csv("students.csv")
students_df.iat[0]
