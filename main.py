import argparse

from dateutil.parser import parse

from atslib import Downloader, Portfolio, Viewer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stocks', required=True)
    parser.add_argument('--window', nargs='+', type=int, default=[10, 20, 50, 100, 200])
    parser.add_argument('--fr', required=True)
    parser.add_argument('--to', required=True)
    parser.add_argument('--strategy', choices=['lo', 'hi', 'avg'], default='lo')
    parser.add_argument('--output', choices=['graph', 'inline', 'db'], default='graph')
    args = parser.parse_args()

    stock_code_list = []
    if args.stocks:
        stock_code_list = args.stocks.split(',')
        map(str.strip, stock_code_list)

    try:
        from_date = parse(args.fr)
        to_date = parse(args.to)
    except (ValueError, TypeError):
        raise SyntaxError("Invalid dates")

    strategy = args.strategy
    view_type = args.output

    # Downloading all the prices
    dl = Downloader()
    for s in stock_code_list:
        dl.add(s)

    stock_list = dl.run()

    # create a portfolio with the stocks
    p = Portfolio(stock_list)
    x, ys = p.calc_sma(from_date, to_date, strategy, args.window)

    v = Viewer.create(view_type, x)
    for idx, y in enumerate(ys):
        v.add_series(y, "%d days" % args.window[idx])

    v.view()


if __name__ == "__main__":
    main()
