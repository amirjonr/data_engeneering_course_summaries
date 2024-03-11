from airflow import DAG
from airflow.utils.dates import days_ago
from operators.ram_species_count_operator_with_custom_hook import RamDeadOrAliveCountOperator

with DAG(
        dag_id='rick_and_morty_api_with_custom_hook',
        default_args={
            'owner': 'amirjon',
            'depends_on_past': False
        },
        start_date=days_ago(0),
        schedule_interval='@once',
        tags=['karpov_courses']
) as dag:
    load_ram = RamDeadOrAliveCountOperator(
        task_id='load_ram',
        dead_or_alive='Dead'
    )
