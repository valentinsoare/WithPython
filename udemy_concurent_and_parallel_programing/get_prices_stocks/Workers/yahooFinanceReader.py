# yahooFinanceReader.py

import requests
from lxml import html
from queue import Empty
from threading import Thread


class YahooFinancePriceScheduler(Thread):
    def __init__(self, input_queue, **kwargs):
        super(YahooFinancePriceScheduler, self).__init__(**kwargs)
        self._input_queue = input_queue
        self.start()

    def run(self):
        while True:
            try:
                value = self._input_queue.get(timeout=5)
            except Empty:
                print('Timeout reached, stopping')
                break

            if value == 'DONE':
                break

            yahoo_finance_reader_worker = YahooFinanceReaderWorker(symbol=value)
            price, symbol_to_print = yahoo_finance_reader_worker.get_price()
            print(f"{symbol_to_print} - {price}")


class YahooFinanceReaderWorker:
    def __init__(self, symbol):
        self.symbol: str = symbol
        base_url = 'https://finance.yahoo.com/quote/'
        self._url: str = f'{base_url}{self.symbol}'

    @property
    def symbol(self) -> str:
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: str) -> None:
        self._symbol = symbol

    def get_price(self) -> tuple:
        r = requests.get(self._url)
        page_contents = html.fromstring(r.text)
        price: str = 'None'

        try:
            price = page_contents.xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/div/div[3]/div[1]/div[1]/fin-streamer[1]')[0].text
        except IndexError:
            pass

        return price, self._symbol
