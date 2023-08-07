from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

params = {
    "p1": "v1",
    "p2": "v2"
}

# params argument
with DAG('params_argument', start_date=days_ago(2), params=params):
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo {{ params.p1 }}', # Output: v1
    )

    task2 = BashOperator(
        task_id='task2',
        bash_command='echo {{ params.p2 }} {{ params.p3}}', # Output: v2 v3
        params={
            "p3": "v3"
        }
    )

task1 >> task2
