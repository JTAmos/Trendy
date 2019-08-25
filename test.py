### License: GNU GPL v2.0 ###

import trendy
import pandas_datareader as pdr

# Bollinger band test
x = pdr.DataReader('WIKI/AAPL','quandl', '2017-01-01', '2017-12-31')
x = x.reindex(index=x.index[::-1])
print (trendy.bbands(x,length=20, numsd=2))