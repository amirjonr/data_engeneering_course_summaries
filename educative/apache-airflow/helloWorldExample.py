from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# default list of arguments that can be passed to any of
# the tasks
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['amirshorakhimov0017@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # Parameters that we have commented out but can be specified
    # if desired.
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

# create a DAG
dag = DAG(
    'Example0',
    default_args=default_args,
    description='Example DAG 0',
    schedule_interval='@once', )

# create task to create an empty file with the
# bash command touch. Note, we are passing in the
# bash command through the param bash_command
t1 = BashOperator(
    task_id='create_file',
    bash_command='touch ~/Greet.txt',
    dag=dag, )

# create task to write to file again using the bash
# operator
t2 = BashOperator(
    task_id='write_to_file',
    bash_command='echo "Hello World !" > ~/Greet.txt',
    dag=dag, )

# create task to read the file using the cat bash
# command.
t3 = BashOperator(
    task_id='read_from_file',
    bash_command='cat ~/Greet.txt',
    dag=dag, )

# Specify the order fo the tasks.
# t3 depends on t2 and t2 depends on t1
t1 >> t2 >> t3
