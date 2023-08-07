from airflow import DAG
from airflow.datasets import Dataset
from airflow.operators.bash import BashOperator
from datetime import datetime

local_file = Dataset("/tmp/sample.txt")

with DAG(
    dag_id="my_consumer",
    schedule=[local_file],
    start_date=datetime(2023, 7, 1), 
    catchup=False) as dag:

    task_consumer = BashOperator(
        task_id="consumer1",
        bash_command='cat /tmp/sample.txt')
