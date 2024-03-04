from airflow import DAG
from airflow.exceptions import AirflowFailException
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

# default list of arguments that can be passed to any of
# the tasks
default_args = {
    'owner': 'DataJek',
    'depends_on_past': True,
    'start_date': days_ago(1),
    'retries': 0
}

# create a DAG
dag = DAG(
    dag_id='Example12',
    default_args=default_args,
    description='Example DAG 12',
    schedule_interval='@once',

)

# create task1
task1 = BashOperator(
    task_id='task1',
    bash_command='echo "I am task1"',
    dag=dag, )


# define the pythong callable before creating task2
def execute_task2():
    print("I am task2")
    raise AirflowFailException("failed")


# create task2 which is also responsible for branching
task2 = PythonOperator(
    task_id='task2',
    python_callable=execute_task2,
    dag=dag)

# create task3
task3 = BashOperator(
    task_id='task3',
    bash_command='echo "I am task3"',
    dag=dag)

# create task4
task4 = BashOperator(
    task_id='task4',
    bash_command='echo "I am task4"',
    dag=dag, )

# create task5
task5 = BashOperator(
    task_id='task5',
    bash_command='echo "I am task5"',
    dag=dag,
    trigger_rule='all_failed')

# declare the dependencies
task1 >> task2
task2 >> task3
task2 >> task4
task3 >> task5
task4 >> task5
