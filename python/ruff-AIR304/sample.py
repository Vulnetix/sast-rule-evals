# Sample for Ruff rule AIR304: airflow3-dag-dynamic-value
# This file is designed to trigger the AIR304 rule.
# Run: ruff check --select AIR304 <this_file>

from datetime import datetime

from airflow import DAG

dag = DAG(dag_id="my_dag", start_date=datetime.now())
