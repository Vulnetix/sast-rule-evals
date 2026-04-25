# Sample for Ruff rule PD008: pandas-use-of-dot-at
# This file is designed to trigger the PD008 rule.
# Run: ruff check --select PD008 <this_file>

import pandas as pd

students_df = pd.read_csv("students.csv")
students_df.at["Maria"]
