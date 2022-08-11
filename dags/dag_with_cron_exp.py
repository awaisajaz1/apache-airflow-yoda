from asyncio import tasks
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'airflow',
    'retries': 2,
    'email': ['air...@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='cron_job_expression5',
    default_args=default_args,
    description='My first DAG with cron schedule',
    start_date=datetime(2022, 8, 11),
    schedule_interval=timedelta(minutes=2)
    # schedule_interval='36 5 11 08 *'


) as dag:
    task1 = BashOperator(
        task_id='task_first',
        bash_command="echo Hello World"
    )

    task1
