from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

# dag with context manager
with DAG('dynamic_task', start_date=days_ago(2)):
    tasks = []
    for i in range(0, 5):
        # task_id should be unique
        tasks.append(DummyOperator(task_id=f'task_{i}'))
        if i != 0: 
            tasks[i-1] >> tasks[i]
