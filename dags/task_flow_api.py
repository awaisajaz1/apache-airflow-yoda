from asyncio import tasks
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.decorators import dag, task


default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}


@dag(
    dag_id='my_dag_with_task_flow_api',
    default_args=default_args,
    start_date=datetime(2022, 8, 10),
    schedule_interval='@daily')
def etl_flow():

    @task()
    def get_name():
        return 'Owais Own'

    @task()
    def get_age():
        return 32

    @task(multiple_outputs=True)
    def get_job():
        return {
            'job_title': 'Data Engineer',
            'company': 'Qorelogix'
        }

    @task()
    def greet_user(name, age, job_title, company):
        print(
            f"My name is {name} and i am {age} years old and I am a {job_title} at {company}")

    name = get_name()
    age = get_age()
    get_job_info = get_job()
    greet_user(
        name, age, job_title=get_job_info['job_title'], company=get_job_info['company'])


greet_all = etl_flow()
