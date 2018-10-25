import multiprocessing as mp
import requests
from .stock import Stock


def worker(stock_code):
    url = 'https://stooq.com/q/d/l/?s={stock_code}.US&i=d'.format(stock_code=stock_code)
    r = requests.get(url, allow_redirects=True)
    if r.status_code == requests.codes.ok:
        s = Stock(stock_code)
        s.load(r.content)
        s.ready = True
        print s
        return s


class Downloader(object):
    def __init__(self):
        self.stock_code_list = set()

    def add(self, stock_code):
        self.stock_code_list.add(stock_code)

    def run(self):
        pool = mp.Pool(mp.cpu_count() * 2)

        pool_outputs = pool.map(worker, self.stock_code_list)
        pool.close()
        pool.join()
        return pool_outputs
