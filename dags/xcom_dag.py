from asyncio import tasks
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator


# python fucntion
def get_name():
    return 'Owais'


def bio_data(age, ti):
    name = ti.xcom_pull(task_ids='python_task_first')
    print(f"My name is {name} and i am {age} years old")


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}


with DAG(
    dag_id='my_python_dag',
    default_args=default_args,
    description='My first Python DAG is in testing mode',
    start_date=datetime(2022, 8, 3, 2),
    schedule_interval='@daily'

) as dag:
    task1 = PythonOperator(
        task_id='python_task_second',
        python_callable=bio_data,
        op_kwargs={'age': 32}
    )

    task2 = PythonOperator(
        task_id='python_task_first',
        python_callable=get_name
    )

    task2 >> task1
