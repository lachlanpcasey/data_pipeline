from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def print_hello():
    return "Hello, Airflow!"

dag = DAG(
    'hello_airflow',
    schedule_interval=timedelta(seconds=10),  # Set the DAG run interval to every minute
    start_date = datetime(year=2023, month=10, day=22),
    catchup=False,
)

hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag,
)

hello_task
