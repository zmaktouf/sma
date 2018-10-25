import utils
from .stock import Stock


class Portfolio(object):

    def __init__(self, stock_list=None):
        self.stock_list = stock_list or []

    def add_stock(self, s):
        if isinstance(s, Stock):
            self.stock_list.append(s)

    def calc_sma(self, from_date, to_date, strategy, window):
        if not isinstance(window, list):
            window = [window]

        # extract reference price for the period stock_list
        # result is a list of dict
        result = [stock.sample(from_date, to_date, strategy) for stock in self.stock_list]
        tmp = utils.aggregate_add(result)

        xs = tmp.keys()
        ys_ = tmp.values()

        ys = []

        for w in window:
            sma = utils.SMA(w)
            ys.append(map(sma, ys_))

        return xs, ys
