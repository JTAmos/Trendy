###**GNU GPL v2.0 modified file notice**
#__12/23/2018 - Changes made by Timothy Yu__
	# Created test.py file for bollinger band func test

import trendy
import pandas_datareader as pdr

# Bollinger band test
x = pdr.DataReader("AAPL", "yahoo")
x = x.reindex(index=x.index[::-1])
print (trendy.bbands(x,length=20, numsd=2))