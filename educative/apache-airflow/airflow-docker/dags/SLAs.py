from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='sla_test',
    default_args=default_args,
    description='SLA test DAG',
    schedule_interval='*/2 * * * *',
    # catchup=False,
    start_date=days_ago(2),

)

task1 = BashOperator(
    task_id='task1',
    bash_command='sleep 65',
    dag=dag,
    sla=timedelta(seconds=1)
)
