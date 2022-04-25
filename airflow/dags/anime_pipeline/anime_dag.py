from utilities import anime_pipeline

"""
# Anime Pipeline
This pipeline will load anime data into the database.

"""

# Built-in packages
from datetime import datetime, timedelta

# Pip packages
from airflow import DAG
from airflow.operators.python import PythonOperator

# Custom function
from utilities import anime_pipeline


default_args = {
    'owner':'Tyson',
    'depends_on_past':False,
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

with DAG(
    "anime_dag",
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 12, 10),
    catchup=False,
    tags=["Animes"]

) as dag:

    grab_data = PythonOperator(task_id="grab_data", 
                                python_callable=anime_pipeline, 
                                )