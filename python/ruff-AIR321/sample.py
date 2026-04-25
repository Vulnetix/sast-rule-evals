# Sample for Ruff rule AIR321: airflow31-moved
# This file is designed to trigger the AIR321 rule.
# Run: ruff check --select AIR321 <this_file>

from airflow.utils.timezone import convert_to_utc
from datetime import datetime

convert_to_utc(datetime.now())
