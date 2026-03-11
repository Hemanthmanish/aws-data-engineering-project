from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    'sales_pipeline',
    start_date=datetime(2024,1,1),
    schedule_interval='@daily'
)

run_etl = BashOperator(
    task_id='run_etl',
    bash_command='python etl/glue_etl_job.py',
    dag=dag
)

run_etl
