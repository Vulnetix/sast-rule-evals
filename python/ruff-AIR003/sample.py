from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sdk import Variable
import datetime

dag = DAG("example", start_date=datetime.datetime(2023, 1, 1))

foo = Variable.get("foo")
BashOperator(task_id="bad", bash_command="echo $FOO", env={"FOO": foo}, dag=dag)
