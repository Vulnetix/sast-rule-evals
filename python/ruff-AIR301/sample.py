# Sample for Ruff rule AIR301: airflow3-removal
# This file is designed to trigger the AIR301 rule.
# Run: ruff check --select AIR301 <this_file>

from airflow.utils.dates import days_ago


yesterday = days_ago(today, 1)
