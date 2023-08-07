from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# Define default arguments for the DAG
default_args = {
    'owner': 'your_name',
    'start_date': datetime(2023, 1, 1),
}

# Create a DAG object
dag = DAG('sample_dag', 
          default_args=default_args,
          schedule_interval='0 0 * * *')

# Define tasks within the DAG
task1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)

def python_function():
    print("Hello, Airflow!")

task2 = PythonOperator(
    task_id='python_task',
    python_callable=python_function,
    dag=dag
)

# Set up task dependencies
task1 >> task2