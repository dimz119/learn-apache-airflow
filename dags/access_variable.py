from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable

def _access_variable(ti):
    print("printing variable info....")
    # too many connection
    print(Variable.get("var1"))
    print(Variable.get("var2"))

    # recommended way
    var_dict = Variable.get("var_dict", deserialize_json=True)
    print(var_dict['var1'])
    print(var_dict['var2'])
    print("ended")

# dag with context manager
with DAG('access_variable', start_date=days_ago(2)):
    task_extract_data_op = PythonOperator(
        task_id="extract_data_op",
        python_callable=_access_variable,
        provide_context=True
    )
