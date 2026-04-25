# Sample for Ruff rule AIR003: airflow-variable-get-outside-task
# This file is designed to trigger the AIR003 rule.
# Run: ruff check --select AIR003 <this_file>

from airflow.sdk import Variable
from airflow.operators.bash import BashOperator


foo = Variable.get("foo")
BashOperator(task_id="bad", bash_command="echo $FOO", env={"FOO": foo})
