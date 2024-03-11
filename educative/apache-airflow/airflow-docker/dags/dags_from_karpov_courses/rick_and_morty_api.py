import logging

import requests
from airflow import AirflowException, DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def get_page_count(api_url):
    """
    Get count of page in API
    :param api_url:
    :return: page_count
    """
    r = requests.get(api_url)
    if r.status_code == 200:
        logging.info('Successfully fetched')
        page_count = r.json().get('info').get('pages')
        logging.info('Page count is {}'.format(page_count))
        return page_count
    else:
        logging.error('Http status code is {}'.format(r.status_code))
        raise AirflowException('Error in load page count')


def get_human_count_on_page(result_json):
    human_count_on_page = 0
    for one_char in result_json:
        if one_char.get('species') == 'Human':
            human_count_on_page += 1
        logging.info('Human count on page is {}'.format(human_count_on_page))
        return human_count_on_page


def load_ram_func():
    """
    Logging count of human in Rick&Morty
    :return: None
    """
    human_count = 0
    ram_char_url = 'https://rickandmortyapi.com/api/character?page={pg}'
    for page in range(get_page_count(ram_char_url.format(pg='1'))):
        r = requests.get(ram_char_url.format(pg=str(page + 1)))
        if r.status_code == 200:
            logging.info(f'Page {page + 1}')
            human_count += get_human_count_on_page(r.json().get('results'))
        else:
            logging.warning('Http status code is {}'.format(r.status_code))
            raise AirflowException('Error in load from Rick&Morty API')
    logging.info('Human count in Rick&Morty: {}'.format(human_count))


with DAG(
        dag_id='rick_and_morty_api',
        start_date=days_ago(0),
        default_args={
            'owner': 'amirjon',
        },
        schedule_interval='@once',
        tags=['karpov_courses']
) as dag:
    load_ram = PythonOperator(
        task_id='load_ram',
        python_callable=load_ram_func
    )
