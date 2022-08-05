from asyncio import tasks
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator


# python fucntion
def hello_world():
    print("Hello World")
    return "Hello World"


def bio_data(name, age):
    print(f"My name is {name} and i am {age} years old")


default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='my_python_dag',
    default_args=default_args,
    description='My first Python DAG is in testing mode',
    start_date=datetime(2022, 8, 3, 2),
    schedule_interval='@daily'


) as dag:
    task1 = PythonOperator(
        task_id='python_task_first',
        python_callable=hello_world
    )

    task2 = PythonOperator(
        task_id='python_task_second',
        python_callable=bio_data,
        op_kwargs={'name': 'Owais Own', 'age': 32}
    )

    # Task dependencies method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    # task2.set_upstream(task4)

    # Task dependencies method 2
    task1 >> task2

    # Task dependencies method 3
    # task1 >> [task2, task3]
    # task2 >> [task4]
