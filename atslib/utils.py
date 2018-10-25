from collections import Counter, OrderedDict
from collections import deque
from operator import add


def aggregate_add(l):
    # we aggregate the result by summing the values
    unordered_result = reduce(add, (Counter(r) for r in l))

    # we order by key
    result = OrderedDict(sorted(unordered_result.items(), key=lambda item: item[0]))
    return result


class SMA(object):
    def __init__(self, window):
        self.window = int(window)
        self.working_deq = deque()

    def __call__(self, price):
        deq = self.working_deq
        result = None

        deq.append(price)

        if len(deq) == self.window:
            result = float(sum(deq)) / self.window
            deq.popleft()

        return result
