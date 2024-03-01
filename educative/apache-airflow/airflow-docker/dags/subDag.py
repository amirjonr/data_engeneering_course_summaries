from airflow import DAG
from airflow.operators.bash import BashOperator


def generate_sub_dag(parent_dag_name, sub_dag_name, args):
    subDag = DAG(
        dag_id='%s.%s' % (parent_dag_name, sub_dag_name),
        default_args=args,
        schedule_interval='@daily',
    )

    # create task3
    task3 = BashOperator(
        task_id='task3',
        bash_command='echo "I am task3"',
        dag=subDag
    )

    # create task4
    task4 = BashOperator(
        task_id='task4',
        bash_command='echo "I am task4"',
        dag=subDag
    )

    # create task3
    task5 = BashOperator(
        task_id='task5',
        bash_command='echo "I am task5"',
        dag=subDag
    )

    task6 = BashOperator(
        task_id='task',
        dag=subDag,
        bash_command='echo "I am task6"'
    )

    task6 >> [task3, task4, task5]

    return subDag
