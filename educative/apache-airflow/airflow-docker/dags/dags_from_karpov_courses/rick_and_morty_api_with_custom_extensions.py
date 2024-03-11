from datetime import timedelta

from airflow import DAG
from airflow.utils.dates import days_ago
from operators.ram_species_count_operator import RamSpeciesCountOperator

with DAG(
        dag_id='rick_and_morty_api_with_custom_extensions',
        default_args={
            'owner': 'amirjon',
            'depends_on_past': False,
            'retry': 5,
            'retry_delay': timedelta(minutes=5)
        },
        start_date=days_ago(0),
        schedule_interval='@once',
        tags=['karpov_courses']
) as dag:
    load_ram = RamSpeciesCountOperator(
        task_id='load_ram',
        species_type='Alien'
    )
