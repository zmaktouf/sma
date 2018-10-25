import sys
import unittest


class UtilsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, '..')

    @classmethod
    def tearDownClass(cls):
        sys.path.pop(0)

    def test_aggregate_add_same_len(self):
        from atslib import aggregate_add
        from collections import OrderedDict

        dict1 = {"b": 2, "a": 1, "c": 3}
        dict2 = {"b": 4, "a": 2, "c": 6}

        r = aggregate_add([dict1, dict2])
        expected = OrderedDict()
        expected["a"] = 3
        expected["b"] = 6
        expected["c"] = 9

        self.assertEqual(expected, r)

    def test_aggregate_add_diff_len(self):
        from atslib import aggregate_add
        from collections import OrderedDict

        dict1 = {"b": 2, "a": 1, "c": 3, "d": 10}
        dict2 = {"b": 4, "a": 2, "c": 6, "e": 20, "f": 30}

        r = aggregate_add([dict1, dict2])
        expected = OrderedDict()
        expected["a"] = 3
        expected["b"] = 6
        expected["c"] = 9
        expected["d"] = 10
        expected["e"] = 20
        expected["f"] = 30

        self.assertEqual(expected, r)

    def test_SMA_1(self):
        from atslib import SMA

        sma = SMA(1)

        ll = map(sma, [1, 2, 3, 4, 5])

        self.assertListEqual([1, 2, 3, 4, 5], ll)

    def test_SMA_2(self):
        from atslib import SMA

        sma = SMA(2)

        ll = map(sma, [1, 2, 3, 4, 5])

        self.assertListEqual([None, 1.5, 2.5, 3.5, 4.5], ll)

    def test_SMA_3(self):
        from atslib import SMA

        sma = SMA(3)

        ll = map(sma, [1, 2, 3, 4, 5])

        self.assertListEqual([None, None, 2, 3, 4], ll)

    def test_SMA_4(self):
        from atslib import SMA

        sma = SMA(4)

        ll = map(sma, [1, 2, 3, 4, 5])

        self.assertListEqual([None, None, None, 2.5, 3.5], ll)

    def test_SMA_5(self):
        from atslib import SMA

        sma = SMA(5)

        ll = map(sma, [1, 2, 3, 4, 5])

        self.assertListEqual([None, None, None, None, 3], ll)

    def test_SMA_6(self):
        from atslib import SMA

        sma = SMA(6)

        ll = map(sma, [1, 2, 3, 4, 5])

        self.assertListEqual([None, None, None, None, None], ll)
