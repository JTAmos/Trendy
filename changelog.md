# Changelog
License: GNU GPL v2.0 

## 12/23/2018 - Changes made by Timothy Yu
- `runtests.py` created for numpy 1.12.1 version check
  - Created  `environment.yml` (anaconda/conda) for package requirements; current code for `minitrends()` requires numpy `1.12.1` or lower to function properly without a rewrite or reimplementation of local minima/maximia detection
    - Behavior of masked arrays has changed above numpy `1.12.1`; minima/maxima code for minitrends() requires rewrite or reimplemention for newer numpy versions
    - Reference/discussion about this issue on an unrelated repository/project:
    - https://github.com/dereneaton/ipyrad/issues/253#issuecomment-317842437`

- Created `test.py` file for bollinger band func test
     - Yahoo finance datareader import replaced by Quandl - yahoo finance API deprecated 
  
- trendy.py
    - Incorporated "[bug in gentrends #1](https://github.com/dysonance/Trendy/issues/1)" PR fix by fraka6 into `segtrends()`.
    - Moved imports to beginning of trendy.py + removed redundant imports
    - Updated pandas_datareader import from `pandas.io.data` 
    - Added bbands function from [kimtaesu fork](https://github.com/kimtaesu/Trendy/commit/29fc88a35f3a701b9e2c309957cb23bb6d1c9f78) 
- `LICENSE.txt` update with original creator copyright + name as per GPL v2.0

   