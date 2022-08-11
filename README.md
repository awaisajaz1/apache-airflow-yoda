# apache-airflow-yoda

Install Airflow Directly on Linux/Ubuntu
## To create a python virtual environment
python -n venv venv
pip install apache-airflow==2.0.1 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.0.1/constraints-3.7.txt"



## Setup Airflow using docker compose
docker-compose up airflow-init
docker-compose up    <-d>
docker ps
http://localhost:8080    > airflow / airflow 
docker-compose down --volumes --rmi all
docker-compose down -v
