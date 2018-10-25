import csv
from StringIO import StringIO

from dateutil.parser import parse
from collections import OrderedDict


class Stock(object):
    def __init__(self, code):
        self.code = code
        self.raw_data = []
        self.ready = False

    def __repr__(self):
        return "Stock(%s) %d ticks" % (self.code, len(self.raw_data))

    def __eq__(self, other):
        if isinstance(other, Stock):
            return self.code == other.code
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__repr__())

    def load(self, csv_stream):
        f = StringIO(csv_stream)
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            self.raw_data.append(row)

    def _get_data(self, from_date, to_date):

        def _in_range(f, t):
            return lambda x: f <= x <= t

        try:
            fr = from_date
            to = to_date
            if isinstance(fr, str):
                fr = parse(fr)
            if isinstance(to, str):
                to = parse(to)

            assert fr <= to

            in_range = _in_range(fr, to)

            result = list(filter(lambda el: in_range(parse(el['Date'])), self.raw_data))
            return result

        except ValueError:
            return []

    def sample(self, from_date, to_date, ref_price, convert_date=True):

        def _value(col_name, elem):
            if type(col_name) == tuple:
                return (float(elem[col_name[0]]) + float(elem[col_name[1]])) / 2
            else:
                return float(elem[col_name])

        assert ref_price in ['lo', 'hi', 'avg']
        result = self._get_data(from_date, to_date)

        column_name = {'lo': 'Low', 'hi': 'High', 'avg': ('Low', 'High')}[ref_price]

        xy = OrderedDict()
        for el in result:
            xy[parse(el['Date'])] = _value(column_name, el)
            # xy[el['Date']] =

        return xy
