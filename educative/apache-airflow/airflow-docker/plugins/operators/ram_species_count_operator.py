import logging
from typing import Any

import requests
from airflow import AirflowException
from airflow.models import BaseOperator
from airflow.utils.context import Context


class RamSpeciesCountOperator(BaseOperator):
    """
    Count of dead concrete species
    """
    template_fields = ('species_type',)
    ui_color = '#e0ffff'

    def __init__(self, species_type: str = 'Human', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.species_type = species_type

    def execute(self, context: Context) -> Any:
        """
        Logging count of concrete species in Rick&Morty
        :param context:
        :return: any
        """
        species_count = 0
        ram_char_url = 'https://rickandmortyapi.com/api/character?page={pg}'
        for page in range(self.get_page_count(ram_char_url.format(pg='1'))):
            import requests
            r = requests.get(ram_char_url.format(pg=str(page + 1)))
            if r.status_code == 200:
                logging.info(f'Page {page + 1}')
                species_count += self.get_species_count_on_page(r.json().get('results'))
            else:
                logging.warning('Http status code is {}'.format(r.status_code))
                raise AirflowException('Error in load from Rick&Morty API')
        logging.info('{} count in Rick&Morty: {}'.format(self.species_type, species_count))

    def on_kill(self) -> None:
        logging.info('here we killed opened resources')

    def get_page_count(self, api_url):
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

    def get_species_count_on_page(self, result_json):
        human_count_on_page = 0
        for one_char in result_json:
            if one_char.get('species') == self.species_type:
                human_count_on_page += 1
            logging.info('{} count on page is {}'.format(self.species_type, human_count_on_page))
            return human_count_on_page
