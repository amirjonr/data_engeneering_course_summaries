from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['amirshorakhimov0017@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


def greet_name(ti):
    name = ti.xcom_pull(task_ids='task1', key='name')
    print(f"Hello {name}!")


def get_name(ti):
    ti.xcom_push(key='name', value='Amirjon')


with DAG(
        dag_id="ExampleV3Dag",
        schedule_interval='@once',
        description='This is my first DAG',
        default_args=default_args,
) as dag:
    task1 = PythonOperator(
        task_id='task1',
        python_callable=get_name,
        dag=dag,
    )

    task2 = PythonOperator(
        task_id='task2',
        python_callable=greet_name,
        dag=dag,
    )

    task3 = BashOperator(
        task_id='task3',
        bash_command='echo {{ ti.xcom_pull(task_ids="task1", key="name") }}',
        dag=dag,
    )

    task1 >> [task3, task2]
