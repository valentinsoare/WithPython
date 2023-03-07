#!/usr/bin/python

from time import time
from multiprocessing import Queue
from Workers.wikiWorker import WikiWorker
from Workers.yahooFinanceReader import YahooFinancePriceScheduler


def main():
    symbol_queue = Queue()
    scraper_start = time()

    wiki_worker = WikiWorker()
    yahoo_finance_price_scheduler_threads: list = []
    num_yahoo_finance_price_workers = 4

    for i in range(num_yahoo_finance_price_workers):
        yahoo_finance_scheduler = YahooFinancePriceScheduler(input_queue=symbol_queue)
        yahoo_finance_price_scheduler_threads.append(yahoo_finance_scheduler)

    for j in wiki_worker.get_sp_500_companies():
        symbol_queue.put(j)

    for k in range(len(yahoo_finance_price_scheduler_threads)):
        symbol_queue.put('DONE')

    for i in yahoo_finance_price_scheduler_threads:
        i.join()

    print(f"Extracting time: {round(time.time() - scraper_start, 1)}")


if __name__ == '__main__':
    main()
