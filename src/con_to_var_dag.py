from airflow.models import Variable, Connection
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

def con_to_var(**context):
  con = Connection.get_connection_from_secrets('custom_conn_id')
  
  Variable.set('host', con.host, serialize_json=True)
  Variable.set('password ', con.password, serialize_json=True)
  Variable.set('login', con.login, serialize_json=True)
  


with DAG(
    dag_id='con_to_var',
    schedule_interval='@daily',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=10)) as dag:

    to_var = PythonOperator(
        task_id='to_var',
        python_callable=con_to_var
    )

    to_var
