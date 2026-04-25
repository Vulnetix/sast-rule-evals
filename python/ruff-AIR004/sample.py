# Sample for Ruff rule AIR004: airflow-task-branch-as-short-circuit
# This file is designed to trigger the AIR004 rule.
# Run: ruff check --select AIR004 <this_file>

from airflow.decorators import task


@task.branch
def my_task():
    if condition:
        return ["my_downstream_task"]
    return []
