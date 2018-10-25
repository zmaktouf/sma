import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from prettytable import PrettyTable


class Viewer(object):
    def __init__(self):
        pass

    @staticmethod
    def create(view_type, x):
        if view_type == 'graph':
            return GraphViewer(x)
        elif view_type == 'inline':
            return ConsoleViewer(x)
        else:
            raise AssertionError("Bad Viewer creation: " + view_type)

    def view(self):
        raise NotImplementedError


class GraphViewer(Viewer):
    def __init__(self, x):
        super(GraphViewer, self).__init__()
        self.x = x or []
        self.ys = []  # List of list
        self.labels = []

    def add_series(self, y, label):
        if isinstance(y, list):
            self.ys.append(y)
            self.labels.append(label)

    def view(self):
        fig, axs = plt.subplots(figsize=(15, 7))

        for idx, y in enumerate(self.ys):
            axs.plot_date(self.x, y, label=self.labels[idx], fmt='-')

        axs.legend()
        axs.grid(True)

        # format the ticks
        axs.xaxis.set_major_locator(mdates.MonthLocator())
        axs.xaxis.set_minor_locator(mdates.WeekdayLocator())
        axs.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

        fig.autofmt_xdate()
        plt.show()


class ConsoleViewer(Viewer):
    def __init__(self, x):
        super(ConsoleViewer, self).__init__()
        self.x = x or []
        self.ys = []  # List of list
        self.labels = []

    def add_series(self, y, label):
        if isinstance(y, list):
            self.ys.append(y)
            self.labels.append(label)

    def view(self):
        t = PrettyTable()

        t.add_column("Date", [d.strftime("%Y-%m-%d") for d in self.x], 'l', 'm')

        for idx, y in enumerate(self.ys):
            t.add_column(self.labels[idx], ['{:20,.2f}'.format(price or 0) for price in y], 'r', 'm')

        print t
