from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="demo", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:
    # Tasks are represented as operators
    hello = BashOperator(
        task_id="hello",
        bash_command="echo Hello from Bash"
    )

    def new_airflow():
        print(datetime.now())
        print("Hello from Airflow python operator!")

    t2 = PythonOperator(
        task_id="airflow",
        python_callable=new_airflow
    )

    @task()
    def new_airflow():
        print(datetime.now())
        print("Hello from Airflow!")

    # Set dependencies between tasks
    hello >> airflow()