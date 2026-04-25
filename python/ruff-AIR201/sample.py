# Sample for Ruff rule AIR201: airflow-xcom-pull-in-template-string
# This file is designed to trigger the AIR201 rule.
# Run: ruff check --select AIR201 <this_file>

from airflow.operators.python import PythonOperator


task_1 = PythonOperator(task_id="task_1", python_callable=my_func)
task_2 = PythonOperator(
    task_id="task_2",
    op_args="{{ ti.xcom_pull(task_ids='task_1') }}",
)
