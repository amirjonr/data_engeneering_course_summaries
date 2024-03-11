from airflow.providers.http.hooks.http import HttpHook


class RickAndMortyHook(HttpHook):
    """
    Interact with Rick and Morty
    """

    def __init__(self, http_conn_id: str, **kwargs) -> None:
        super().__init__(http_conn_id=http_conn_id, **kwargs)
        self.method = 'GET'

    def get_char_page_count(self):
        """
        Returns count of pages in API
        :return: str
        """
        return self.run('api/character').json()['info']['pages']

    def get_char_page(self, page_num: str) -> list:
        """
        Returns count of characters in API
        :return:
        """
        return self.run(f'api/character?page={page_num}').json()['results']
