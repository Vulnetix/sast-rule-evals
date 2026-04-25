# Sample for Ruff rule AIR001: airflow-variable-name-task-id-mismatch
# This file is designed to trigger the AIR001 rule.
# Run: ruff check --select AIR001 <this_file>

from airflow.operators import PythonOperator


incorrect_name = PythonOperator(task_id="my_task")
