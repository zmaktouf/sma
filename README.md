# sma
Simple Moving Average calculator

```
usage: main.py [-h] --stocks STOCKS [--window WINDOW [WINDOW ...]] --fr FR
               --to TO [--strategy {lo,hi,avg}] [--output {graph,inline,db}]

optional arguments:
  -h, --help            show this help message and exit
  --stocks STOCKS       Comma separated value of stock codes
  --window WINDOW [WINDOW ...]
                        List of number of days to compute SMA
  --fr FR               First date
  --to TO               Last date
  --strategy {lo,hi,avg}
                        Reference price
  --output {graph,inline,db}
                        Visualization type
```

Example
```console
$ python main.py  --stocks FB,TSLA,AAPL --fr 2017-01-01 --to 2018-09-30 --window 20 50 100 200 --output graph
```
