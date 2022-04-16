from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

def create_dag(dag_id,
               dag_number,
               default_args,
               schedule='@daily'):

    dag = DAG(dag_id,
              schedule_interval=schedule,
              default_args=default_args)

    with dag:
        [DummyOperator(task_id=f'task_{i}') for i in range(0, 10)]

    return dag


for n in range(1, 6):
    dag_id = f'dag_{n}'

    default_args = {'owner': 'airflow', 'start_date': datetime(2021, 1, 1)}
    dag_number = n
    
    globals()[dag_id] = create_dag(dag_id, dag_number, default_args)