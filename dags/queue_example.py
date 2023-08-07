from airflow import DAG
from airflow.datasets import Dataset
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="queue_example",
    schedule="0 0 * * *",
    start_date=datetime(2023, 7, 1),
    catchup=False) as dag:

    task_producer1 = BashOperator(
        task_id="sleep_1",
        queue="cpu_intensive",
        bash_command='sleep 20')

    task_producer2 = BashOperator(
        task_id="sleep_2",
        queue="io_intensive",
        bash_command='sleep 20')

task_producer1 >> task_producer2
