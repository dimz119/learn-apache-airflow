import json
import random
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

def generate_number(ti):
    number = random.randint(0, 100)
    print(f"Generated number: {number}")
    # push the integer
    ti.xcom_push(
        key='random_number',
        value=number)
    # # push the json
    # ti.xcom_push(
    #     key='random_number',
    #     value=json.dumps({"v": number}))

def read_number(ti):
    number = ti.xcom_pull(
            key='random_number',
            task_ids='generate_number_task')
    print(f"Received number: {number}")

with DAG(
    dag_id="xcom_dag",
    start_date=days_ago(2),
    schedule="@daily",
    default_args={"retries": 1},
):
    # provide_context: PythonOperator allows the task instance (ti) to be passed to the Python callable
    generate_number_task = PythonOperator(
        task_id='generate_number_task',
        python_callable=generate_number,
        provide_context=True)

    read_number_task = PythonOperator(
        task_id='read_number_task',
        python_callable=read_number,
        provide_context=True)

generate_number_task >> read_number_task
