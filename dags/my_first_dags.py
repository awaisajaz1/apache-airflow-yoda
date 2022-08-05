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
        bash_command="echo Hello People"
    )

    task3 = BashOperator(
        task_id='task_three',
        bash_command="echo I am partner of task_first"
    )

    task4 = BashOperator(
        task_id='task_four',
        bash_command="echo I am partner of task_second"
    )

    task5 = BashOperator(
        task_id='task_five',
        bash_command="python /opt/airflow/landings/hello_landing.py"

    )

    # Task dependencies method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    # task2.set_upstream(task4)

    # Task dependencies method 2
    task1 >> task2 >> task3
    task2 >> task4
    task1 >> task5

    # Task dependencies method 3
    # task1 >> [task2, task3]
    # task2 >> [task4]
