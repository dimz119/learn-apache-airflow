from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

with DAG('list_task_dag', start_date=days_ago(2)):
    task1 = DummyOperator(task_id='task1')
    task2 = DummyOperator(task_id='task2')
    task3 = DummyOperator(task_id='task3')
    task4 = DummyOperator(task_id='task4')
    task5 = DummyOperator(task_id='task5')

# normal way
# task1 >> task2
# task1 >> task3
# task1 >> task4
# task2 >> task5
# task3 >> task5
# task4 >> task5

# better way with list
task1 >> [task2, task3, task4] >> task5