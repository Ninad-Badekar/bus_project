from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 9, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG("bus_pipeline",
         default_args=default_args,
         schedule_interval="* * * * *",  # every minute
         catchup=False) as dag:

    generate = BashOperator(
        task_id="generate_data",
        bash_command="python3 /path/to/generate_data.py"
    )

    produce = BashOperator(
        task_id="produce_data",
        bash_command="python3 /path/to/producer.py"
    )

    generate >> produce
