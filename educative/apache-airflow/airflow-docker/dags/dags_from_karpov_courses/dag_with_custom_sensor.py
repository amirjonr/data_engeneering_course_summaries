from airflow import DAG
from airflow.utils.dates import days_ago
from operators.random_sensor import RandomSensor

with DAG(
        dag_id='dag_with_custom_sensor',
        start_date=days_ago(0),
        default_args={
            'owner': 'amirjon',
        },
        schedule_interval='@once',
        tags=['karpov_courses']
) as dag:
    random_sensor = RandomSensor(
        task_id='random_sensor',
        mode='reschedule',
        range_number=10
    )
