from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.base_hook import BaseHook
from airflow.utils.dates import days_ago

def _access_connection(ti):
    print("printing connection info....")
    print(BaseHook.get_connection('my_postgres_connection').host)
    print(BaseHook.get_connection('my_postgres_connection').password)
    print("ended")

# dag with context manager
with DAG('connection_access', start_date=days_ago(2)):
    task_extract_data_op = PythonOperator(
        task_id="extract_data_op",
        python_callable=_access_connection,
        provide_context=True
    )
