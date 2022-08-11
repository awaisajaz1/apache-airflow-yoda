# apache-airflow-yoda

Install Airflow Directly on Linux/Ubuntu
## To create a python virtual environment
python -n venv venv <br />
pip install apache-airflow==2.0.1 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.0.1/constraints-3.7.txt" <br />



## Setup Airflow using docker compose
docker-compose up airflow-init <br />
docker-compose up    <-d> <br />
docker ps <br />
http://localhost:8080    > airflow / airflow  <br />
docker-compose down --volumes --rmi all <br />
docker-compose down -v <br />
