from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
import os


LOG_PATH = os.getenv('AIRFLOW_LOG_FOLDER', '/root/airflow/logs')

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='cleanup_airflow_log',
    default_args=args,
    schedule_interval='@daily',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=10)) as dag:

  remove_logs = BashOperator(
      task_id='remove_logs',
      bash_command='rm -r $airflow_logs',
      env={'airflow_logs': LOG_PATH}
  )

  remove_logs
