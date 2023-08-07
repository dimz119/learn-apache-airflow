from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

with DAG('trigger_rule_example', start_date=days_ago(2)):
    task1 = DummyOperator(task_id='task1')
    task2 = DummyOperator(task_id='task2')

    task3 = DummyOperator(
        task_id='task3',
        trigger_rule='one_success'
    )

task1 >> task3
task2 >> task3
