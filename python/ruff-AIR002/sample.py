# Sample for Ruff rule AIR002: airflow-dag-no-schedule-argument
# This file is designed to trigger the AIR002 rule.
# Run: ruff check --select AIR002 <this_file>

from airflow import DAG


# Using the implicit default schedule.
dag = DAG(dag_id="my_dag")
