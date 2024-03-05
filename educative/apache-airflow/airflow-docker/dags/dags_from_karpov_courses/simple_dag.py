"""
This is simple DAG.
It consists of Sensor that waits 6 am,
Bash Operator that logs execution_date
and two Python Operators that prints some text.
"""
import logging
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.time_delta import TimeDeltaSensor
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'amirjon',  # responsible for dag
    'start_date': days_ago(12),  # generates 12 DAG instances till 12 days ago
    'poke_interval': 600  # restart time for sensor
}

dag = DAG(
    dag_id='simple_dag',
    default_args=default_args,
    schedule_interval='@daily',
    max_active_runs=1,
    tags=['karpov_courses']
)

wait_until_6am = TimeDeltaSensor(
    task_id='wait_until_6am',
    delta=timedelta(seconds=6 * 60 * 60),
    dag=dag
)

echo_ds = BashOperator(
    task_id='echo_ds',
    bash_command='echo {{ ds }}',
    dag=dag
)


def first_func():
    logging.info('First log')


def second_func():
    logging.info('Second log')


first_task = PythonOperator(
    task_id='first_task',
    python_callable=first_func,
    dag=dag
)

second_task = PythonOperator(
    task_id='second_task',
    python_callable=second_func,
    dag=dag
)

wait_until_6am >> echo_ds >> [first_task, second_task]

dag.doc_md = __doc__

wait_until_6am.doc_md = """Sensor, waits until 6am by Greenwich"""
echo_ds.doc_md = """Logs execution_date"""
first_task.doc_md = """Logs First log"""
second_task.doc_md = """Logs Second log"""
