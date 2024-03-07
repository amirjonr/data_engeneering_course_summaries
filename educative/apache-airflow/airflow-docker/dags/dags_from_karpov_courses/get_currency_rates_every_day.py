"""
Get data from CBR to postgres
"""

import csv
import logging
from xml.etree import ElementTree

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'amirjon',
    'depends_on_past': False,
    'start_date': days_ago(0),
    'email': ['amirshorakhimov0017@gmail.com']
}


def from_xml_to_csv_func():
    parser = ElementTree.XMLParser(encoding='UTF-8')
    tree = ElementTree.parse('/opt/airflow/cur_rates.xml',
                             parser=parser)
    root = tree.getroot()

    with open('/opt/airflow/cur_rates.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for Valute in root.findall('Valute'):
            NumCode = Valute.find('NumCode').text
            CharCode = Valute.find('CharCode').text
            Nominal = Valute.find('Nominal').text
            Name = Valute.find('Name').text
            Value = Valute.find('Value').text
            writer.writerow(
                [root.attrib['Date']] + [Valute.attrib['ID']] + [NumCode] +
                [CharCode] + [Nominal] + [Name] + [Value.replace(',', '.')])
            logging.info([root.attrib['Date']] + [Valute.attrib['ID']] + [NumCode] +
                         [CharCode] + [Nominal] + [Name] + [Value.replace(',', '.')])


def load_csv_to_postgres_func():
    pg_hook = PostgresHook(
        postgres_conn_id='core_reports_db'
    )

    pg_hook.copy_expert(
        sql="COPY currency_rates from STDIN DELIMITER ','",
        filename='/opt/airflow/cur_rates.csv')


with DAG(
        dag_id='load_data_from_cbr',
        schedule_interval='@daily',
        default_args=default_args,
        max_active_runs=1,
        tags=['karpov_courses']
) as dag:
    export_cbr_xml = BashOperator(
        task_id='export_cbr_xml',
        bash_command='curl -sS http://www.cbr.ru/scripts/XML_daily.asp | iconv -f Windows-1251 -t UTF-8 > /opt/airflow/cur_rates.xml'
    )

    from_xml_to_csv = PythonOperator(
        task_id='from_xml_to_csv',
        python_callable=from_xml_to_csv_func
    )

    load_csv_to_postgres = PythonOperator(
        task_id='load_csv_to_postgres',
        python_callable=load_csv_to_postgres_func
    )

export_cbr_xml >> from_xml_to_csv >> load_csv_to_postgres
