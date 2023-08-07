from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.sensors.sql import SqlSensor
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 7, 1)
}

# Define the DAG
with DAG('postgres_loader',
          description='PostgreSQL Loader Example',
          default_args=default_args,
          schedule_interval='0 0 * * *',
          catchup=False) as dag:

    # Task: Execute a SQL query using PostgresOperator
    sql_query = '''
        INSERT INTO sample_table (key, value)
        VALUES ('hello', 'world')
    '''

    postgres_task = PostgresOperator(task_id='execute_sql_query',
                                    postgres_conn_id='my_postgres_connection',
                                    sql=sql_query,
                                    dag=dag)

    sql_sensor = SqlSensor(task_id='wait_for_condition',
                        conn_id='my_postgres_connection',
                        sql="SELECT COUNT(*) FROM sample_table WHERE key='hello'",
                        mode='poke',
                        poke_interval=30,
                        dag=dag)
    
    sql_query_confirm = '''
        INSERT INTO sample_table (key, value)
        VALUES ('sensor', 'confirmed')
    '''

    postgres_confirm_task = PostgresOperator(task_id='execute_sql_confirm_query',
                                    postgres_conn_id='my_postgres_connection',
                                    sql=sql_query_confirm,
                                    dag=dag)
    
postgres_task >> sql_sensor >> postgres_confirm_task
