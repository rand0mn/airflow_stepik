from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.operators.http_operator import SimpleHttpOperator

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='http_to_xcom',
    default_args=args,
    schedule_interval='@daily',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=10)) as dag:

    get_rng = SimpleHttpOperator(
        task_id='http_to_xcom',
        method='GET',
        http_conn_id='random_api',
        endpoint='/integers/?num=1&min=1&max=5&col=1&base=2&format=plain',
        do_xcom_push=True
    )

    get_rng
