from asyncio import tasks
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='my_first_dag',
    default_args=default_args,
    description='My first DAG is in testing mode',
    start_date=datetime(2022, 8, 3, 2),
    schedule_interval='@daily'


) as dag:
    task1 = BashOperator(
        task_id='task_first',
        bash_command="echo Hello World"
    )

    task2 = BashOperator(
        task_id='task_second',
        bash_command="ipconfig"
    )

    task1.set_downstream(task2)
