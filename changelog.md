# Changelog
License: GNU GPL v2.0 

## 12/23/2018 - Changes made by Timothy Yu
	- runtests.py created for numpy 1.12.1 version check
    - Created test.py file for bollinger band func test
         Yahoo finance datareader import replaced by quandl - yahoo finance api deprecrated 
    - trendy.py
        - Incorporated "bug in gentrends #1" PR fix by fraka6 into segtrends().
        - Moved imports to beginning of trendy.py + removed redundant imports
        - Updated pandas_datareader import from `pandas.io.data` 
        - Added bbands function from kimtaesu fork 
            - https://github.com/kimtaesu/Trendy/commit/29fc88a35f3a701b9e2c309957cb23bb6d1c9f78