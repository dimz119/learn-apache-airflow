import time
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.utils.dates import days_ago

def decide_which_path():
    if int(time.time()) % 2 == 0:
        return "even_path_task"
    else:
        return "odd_path_task"

with DAG(
    dag_id="branch_operator_dag",
    start_date=days_ago(2),
    schedule="@daily",
    default_args={"retries": 1},
):
    branch_task = BranchPythonOperator(
        task_id='branch_task',
        python_callable=decide_which_path)

    even_path_task = DummyOperator(task_id='even_path_task')
    odd_path_task = DummyOperator(task_id='odd_path_task')

branch_task >> even_path_task
branch_task >> odd_path_task
