from airflow import DAG
from airflow.datasets import Dataset
from airflow.operators.bash import BashOperator
from datetime import datetime

local_file1 = Dataset("/tmp/sample1.txt")
local_file2 = Dataset("/tmp/sample2.txt")

with DAG(
    dag_id="multiple_producer",
    schedule="0 0 * * *",
    start_date=datetime(2023, 7, 1), 
    catchup=False) as dag:

    task_producer = BashOperator(
        task_id="multiple_producer1",
        bash_command='echo "hello world" >> /tmp/sample1.txt; echo "hello airflow" >> /tmp/sample2.txt',
        outlets=[local_file1, local_file2])
