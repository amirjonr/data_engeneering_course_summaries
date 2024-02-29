import logging

import psycopg2
from airflow.hooks.base import BaseHook
from airflow.models import BaseOperator

log = logging.getLogger(__name__)


class PostgresExampleOperator(BaseOperator):
    def __init__(self, *args, **kwargs):
        super(PostgresExampleOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        conn = BaseHook.get_connection('core_reports_db')

        db = psycopg2.connect(
            host=conn.host,
            port=conn.port,
            db=conn.schema
        )
        cursor = db.cursor()

        cursor.execute('SELECT * FROM branches;')
        for row in cursor.fetchall():
            log.info(row[0])

        db.close()
