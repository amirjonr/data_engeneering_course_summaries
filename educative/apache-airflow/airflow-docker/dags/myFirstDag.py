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


def greetName(name):
    print(f"Hello {name}!")


with DAG(
        dag_id="ExampleV1Dag",
        schedule_interval='@once',
        description='This is my first DAG',
        default_args=default_args,
) as dag:
    pyton_operator1 = PythonOperator(
        task_id='pyton_operator1',
        python_callable=greetName,
        op_kwargs={"name": "Amirjon"},
        dag=dag,
    )

    bash_operator1 = BashOperator(
        task_id='bash_operator1',
        bash_command='pwd',
        dag=dag,
    )

    pyton_operator1 >> bash_operator1
