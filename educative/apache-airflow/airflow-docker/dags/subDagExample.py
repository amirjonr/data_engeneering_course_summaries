from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from airflow.utils.dates import days_ago

from subDag import generate_sub_dag

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='sub_dag_exampleV2',
    default_args=default_args,
    description='Example of subDags',
    schedule_interval='@once'
)

# create a start task
task1 = BashOperator(
    task_id='task1',
    bash_command='echo "I am task1"',
    dag=dag)

# create task2
task2 = BashOperator(
    task_id='task2',
    bash_command='echo "I am task2"',
    dag=dag)

repeatable_actions = SubDagOperator(
    task_id='subDAG',
    subdag=generate_sub_dag('sub_dag_exampleV2', 'subDAG', default_args),
    dag=dag,
)

task7 = BashOperator(
    task_id='task7',
    bash_command='echo "I am task7"',
    dag=dag,
)

task1 >> task2 >> repeatable_actions >> task7

