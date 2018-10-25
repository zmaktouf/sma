import sys
import unittest
from dateutil.parser import parse


class StockTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, '..')

    @classmethod
    def tearDownClass(cls):
        sys.path.pop(0)

    def test_eq(self):
        from atslib import Stock
        self.assertEqual(Stock('FB.US'), Stock('FB.US'))
        self.assertNotEqual(Stock('FB.US'), Stock('MSFT.US'))

    def test_sets(self):
        from atslib import Stock
        container = set()
        container.add(Stock('FB.US'))
        container.add(Stock('FB.US'))
        self.assertEqual(len(container), 1)

    def test_load(self):
        from atslib import Stock

        raw = 'Date,Open,High,Low,Close,Volume\n\
2012-05-18,42.05,45,38,38.23,580438450\n\
2012-05-21,36.53,36.66,33,34.03,169418988\n\
2012-05-22,32.61,33.59,30.94,31,101876406\n\
2012-05-23,31.37,32.5,31.36,32,73678512\n\
2012-05-24,32.95,33.21,31.77,33.03,42560731'

        s = Stock('FB.US')
        s.load(raw)
        self.assertEqual(5, len(s.raw_data))

    def test_get_data(self):
        from atslib import Stock

        raw = 'Date,Open,High,Low,Close,Volume\n\
2012-05-18,42.05,45,38,38.23,580438450\n\
2012-05-21,36.53,36.66,33,34.03,169418988\n\
2012-05-22,32.61,33.59,30.94,31,101876406\n\
2012-05-23,31.37,32.5,31.36,32,73678512\n\
2012-05-24,32.95,33.21,31.77,33.03,42560731'

        s = Stock('FB.US')
        s.load(raw)

        ll = s._get_data('2012-05-18', '2012-05-24')
        self.assertEqual(5, len(ll))

        ll = s._get_data('2012-05-21', '2012-05-23')
        expected = [
            {'Volume': '169418988', 'High': '36.66', 'Low': '33', 'Date': '2012-05-21', 'Close': '34.03',
             'Open': '36.53'},
            {'Volume': '101876406', 'High': '33.59', 'Low': '30.94', 'Date': '2012-05-22', 'Close': '31',
             'Open': '32.61'},
            {'Volume': '73678512', 'High': '32.5', 'Low': '31.36', 'Date': '2012-05-23', 'Close': '32',
             'Open': '31.37'},
        ]

        self.assertListEqual(expected, ll)

        ll = s._get_data('2012-05-23', '2012-05-23')
        expected = [
            {'Volume': '73678512', 'High': '32.5', 'Low': '31.36', 'Date': '2012-05-23', 'Close': '32',
             'Open': '31.37'},
        ]

        self.assertListEqual(expected, ll)

        ll = s._get_data('2012-05-25', '2012-05-25')
        expected = []

        self.assertListEqual(expected, ll)

        with self.assertRaises(AssertionError):
            s._get_data('2012-05-26', '2012-05-25')

    def test_sample(self):
        from atslib import Stock

        raw = 'Date,Open,High,Low,Close,Volume\n\
2012-05-18,42.05,45,38,38.23,580438450\n\
2012-05-21,36.53,36.66,33,34.03,169418988\n\
2012-05-22,32.61,33.59,30.94,31,101876406\n\
2012-05-23,31.37,32.5,31.36,32,73678512\n\
2012-05-24,32.95,33.21,31.77,33.03,42560731'

        s = Stock('FB.US')
        s.load(raw)

        ll = s.sample('2012-05-21', '2012-05-23', 'hi')
        expected = ([parse('2012-05-21'), parse('2012-05-22'), parse('2012-05-23')], [36.66, 33.59, 32.5])

        self.assertListEqual(expected[0], ll.keys())
        self.assertListEqual(expected[1], ll.values())

        ll = s.sample('2012-05-21', '2012-05-23', 'lo')
        expected = ([parse('2012-05-21'), parse('2012-05-22'), parse('2012-05-23')], [33, 30.94, 31.36])

        self.assertListEqual(expected[0], ll.keys())
        self.assertListEqual(expected[1], ll.values())

        ll = s.sample('2012-05-21', '2012-05-23', 'avg')
        expected = ([parse('2012-05-21'), parse('2012-05-22'), parse('2012-05-23')], [34.83, 32.265, 31.93])

        self.assertListEqual(expected[0], ll.keys())
        self.assertListEqual(expected[1], ll.values())
