from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

# normal way
# dag = DAG('dag_with_context', start_date=days_ago(2))
# task1 = DummyOperator(task_id='task1', dag=dag)
# task2 = DummyOperator(task_id='task2', dag=dag)
# task3 = DummyOperator(task_id='task3', dag=dag)

# task1 >> task2 >> task3

# dag with context manager
with DAG('list_task_dag', start_date=days_ago(2)):
    task1 = DummyOperator(task_id='task1')
    task2 = DummyOperator(task_id='task2')
    task3 = DummyOperator(task_id='task3')

task1 >> task2 >> task3
