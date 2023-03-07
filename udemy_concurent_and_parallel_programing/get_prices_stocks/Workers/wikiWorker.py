# wikiWorker.py

import requests
from bs4 import BeautifulSoup


class WikiWorker:
    def __init__(self):
        self.url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

    @staticmethod
    def _extract_companies_symbols(page_html):
        soup = BeautifulSoup(page_html, features="html.parser")
        table = soup.find(id='constituents')
        table_rows = table.find_all('tr')

        for i in table_rows[1:]:
            symbol = i.find('td').text.strip('\n')
            yield symbol

    def get_sp_500_companies(self):
        response = requests.get(self.url)

        if response.status_code != 200:
            print(f"Couldn't get entries from the table")
            return None

        yield from self._extract_companies_symbols(response.text)
