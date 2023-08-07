from airflow import DAG
from airflow.datasets import Dataset
from airflow.operators.bash import BashOperator
from datetime import datetime

local_file1 = Dataset("/tmp/sample1.txt")
local_file2 = Dataset("/tmp/sample2.txt")

with DAG(
    dag_id="multiple_consumer",
    schedule=[local_file1, local_file2],
    start_date=datetime(2023, 7, 1), 
    catchup=False) as dag:

    task_consumer = BashOperator(
        task_id="multiple_consumer1",
        bash_command='cat /tmp/sample1.txt; cat /tmp/sample2.txt')
