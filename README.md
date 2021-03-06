# Welcome to sma

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8bccb90bf4b043589ccda4a81fc0e300)](https://app.codacy.com/app/zmaktouf/sma?utm_source=github.com&utm_medium=referral&utm_content=zmaktouf/sma&utm_campaign=Badge_Grade_Settings)

*sma* is a Simple Moving Average calculator

# Getting started
1. Install python dependencies
```bash
[johndoe:~/projects/sma] $ pip install -r requirements.txt
```
2. Run test
```bash
[johndoe:~/projects/sma] $ python tests/runner.py 
```
3. Execute
```bash
[johndoe:~/projects/sma] $ python main.py  --stocks FB,TSLA,AAPL \
                                           --fr 2017-01-01 \
                                           --to 2018-09-30 \
                                           --window 20 50 100 200 \
                                           --output graph
```
# Help
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
