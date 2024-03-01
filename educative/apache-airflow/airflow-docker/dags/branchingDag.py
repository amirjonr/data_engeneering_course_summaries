from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'DataJek',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


# def execute_task2():
#     print("I am task2")
#
#     # randomly choose one of the branches
#     if random.randint(0, 1) == 0:
#         print("We are choosing to run task3")
#         return 'task3'
#     else:
#         print("We are choosing to run task4")
#         return 'task4'

def execute_task2():
    print("I am task2")

    return ['task3', 'task4']


with DAG(
        dag_id='branching_dag',
        start_date=datetime(2024, 3, 1, 10, 10),
        schedule_interval='@once',
        default_args=default_args,
        description='Branching DAG',
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "I am task1"',
        dag=dag,
    )

    task2 = BranchPythonOperator(
        task_id='task2',
        python_callable=execute_task2,
        dag=dag, )

    # create task3
    task3 = BashOperator(
        task_id='task3',
        bash_command='echo "I am task3"',
        dag=dag, )

    # create task4
    task4 = BashOperator(
        task_id='task4',
        bash_command='echo "I am task4"',
        dag=dag, )

    task1 >> task2
    task2 >> task3
    task2 >> task4
