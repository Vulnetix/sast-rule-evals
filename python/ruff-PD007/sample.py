# Sample for Ruff rule PD007: pandas-use-of-dot-ix
# This file is designed to trigger the PD007 rule.
# Run: ruff check --select PD007 <this_file>

import pandas as pd

students_df = pd.read_csv("students.csv")
students_df.ix[0]  # 0th row or row with label 0?
