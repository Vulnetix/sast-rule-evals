# Sample for Ruff rule AIR311: airflow3-suggested-update
# This file is designed to trigger the AIR311 rule.
# Run: ruff check --select AIR311 <this_file>

from airflow import Dataset


Dataset(uri="test://test/")
