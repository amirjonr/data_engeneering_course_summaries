import logging
from typing import Any

from airflow.models import BaseOperator
from airflow.utils.context import Context
from hooks.rick_and_morty_hook import RickAndMortyHook


class RamDeadOrAliveCountOperator(BaseOperator):
    """
    Count number of dead or alive species on RickAndMortyHook
    """
    template_fields = ('dead_or_alive',)
    ui_color = '#c7ffe9'

    def __init__(self, dead_or_alive: str = 'Dead', **kwargs) -> None:
        super().__init__(**kwargs)
        self.dead_or_alive = dead_or_alive

    def execute(self, context: Context) -> Any:
        """
        Logging count of dead or alive species in Rick&Morty
        :param context:
        :return:
        """
        hook = RickAndMortyHook('rick_and_morty')
        dead_or_alive_count = 0
        for page in range(hook.get_char_page_count()):
            logging.info(f'Page {page + 1}')
            one_page = hook.get_char_page(str(page + 1))
            dead_or_alive_count += self.get_dead_or_alive_count_on_page(one_page)
        logging.info(f'{self.dead_or_alive} in Rick & Morty {dead_or_alive_count}')

    def get_dead_or_alive_count_on_page(self, result_json: list) -> int:
        """
        Get count of dead or alive in one page of character
        :param result_json:
        :return: dead_or_alive_count
        """
        dead_or_alive_count_on_page = 0
        for one_char in result_json:
            if one_char.get('status') == self.dead_or_alive:
                dead_or_alive_count_on_page += 1
        logging.info(f'{self.dead_or_alive} count on page {dead_or_alive_count_on_page}')
        return dead_or_alive_count_on_page
