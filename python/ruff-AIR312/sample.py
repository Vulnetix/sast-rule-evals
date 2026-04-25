# Sample for Ruff rule AIR312: airflow3-suggested-to-move-to-provider
# This file is designed to trigger the AIR312 rule.
# Run: ruff check --select AIR312 <this_file>

from airflow.operators.python import PythonOperator


def print_context(ds=None, **kwargs):
    print(kwargs)
    print(ds)


print_the_context = PythonOperator(
    task_id="print_the_context", python_callable=print_context
)
