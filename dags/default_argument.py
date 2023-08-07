from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

# normal way
# with DAG('list_task_dag', start_date=days_ago(2)):
#     task1 = DummyOperator(task_id='task1')
#     task2 = DummyOperator(task_id='task2')
#     task3 = DummyOperator(task_id='task3')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date':days_ago(2),
}

# using default_args
with DAG('default_argument', default_args=default_args):
    task1 = DummyOperator(task_id='task1')
    task2 = DummyOperator(task_id='task2')
    task3 = DummyOperator(task_id='task3')

task1 >> task2 >> task3
