import logging
from datetime import timedelta

import psycopg2
from airflow import DAG
from airflow.hooks.base import BaseHook
from airflow.models import BaseOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['amirshorakhimov0017@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='test_hook_v4',
    default_args=default_args,
    description='Test DAG for hooks and connections',
    schedule_interval='@once',
)

log = logging.getLogger(__name__)


class PostgresExampleOperator(BaseOperator):
    def __init__(self, *args, **kwargs):
        super(PostgresExampleOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('here your code')
        conn = BaseHook.get_connection('core_reports_db')

        log.info(conn)
        db = psycopg2.connect(
            host=conn.host,
            port=conn.port,
            database=conn.schema,
            user='airflow',
            password='airflow'
        )

        cursor = db.cursor()
        #
        cursor.execute('SELECT * FROM connection;')
        for row in cursor.fetchall():
            log.info(row)

        db.close()


postgres_task = PostgresExampleOperator(
    task_id='postgres_example_operator',
    dag=dag,
)
