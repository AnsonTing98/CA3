from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
        'animal_prediction_app',
        start_date=datetime(2022, 5, 1)
        schedule_interval="@daily",
        catchup=False,
        tags=['v1'],
        )as dag:

    t1 = BashOperator(
            task_id='run_ml_model',
            bash_command='python3 /opt/airflow/dags'
            )

    t2 = BashOperator(
            task_id='run_app',
            bash_command='FLASK_APP=/opt/airflow/dags/app.py flask run --host=0.0.0.0'
            )

    t1>>t2
