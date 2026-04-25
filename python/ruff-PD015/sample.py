# Sample for Ruff rule PD015: pandas-use-of-pd-merge
# This file is designed to trigger the PD015 rule.
# Run: ruff check --select PD015 <this_file>

import pandas as pd

cats_df = pd.read_csv("cats.csv")
dogs_df = pd.read_csv("dogs.csv")
rabbits_df = pd.read_csv("rabbits.csv")
pets_df = pd.merge(pd.merge(cats_df, dogs_df), rabbits_df)  # Hard to read.
