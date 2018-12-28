###**GNU GPL v2.0 modified file notice**

#__12/23/2018 - Changes made by Timothy Yu__
	# Created test.py file for bollinger band func test
#__12/26/2018 - Changes made by Timothy Yu__
	# Yahoo finance datareader import replaced by quandl - yahoo finance api deprecrated 

import trendy
import pandas_datareader as pdr

# Bollinger band test
x = pdr.DataReader('WIKI/AAPL','quandl', '2017-01-01', '2017-12-31')
x = x.reindex(index=x.index[::-1])
print (trendy.bbands(x,length=20, numsd=2))