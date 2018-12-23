trendy
======

Numerical trendline Python algorithms for technical analysis of financial securities.

Installation
------------
1. Clone or download the ZIP file and unpack.
2. Go to the unpacked directory and copy to your Python path. Alternatively, you can place the trendy.py file in an easily reachable directory and import into your current working Python environment with
```python
execfile('/path/to/trendy.py')
```
or
```python
import trendy
```

I am still working on getting this project hosted on the Python Package Index, but for now this at least enables you to start using and gaining familiarity with the algorithms.

Examples
--------
Once the files have been imported, you can implement them with simple function calls. Here are some examples.
```python
# Download Apple price history and save adjusted close prices to numpy array
import pandas_datareader as pdr
x = pdr.DataReader("AAPL", "yahoo")['Adj Close']

# Make some trendlines
import trendy

# Generate general support/resistance trendlines and show the chart
# window < 1 is considered a fraction of the length of the data set
trendy.gentrends(x, window = 1.0/3, charts = True)

# Generate a series of support/resistance lines by segmenting the price history
trendy.segtrends(x, segments = 2, charts = True)  # equivalent to gentrends with window of 1/2
trendy.segtrends(x, segments = 5, charts = True)  # plots several S/R lines

# Generate smaller support/resistance trendlines to frame price over smaller periods
trendy.minitrends(x, window = 30, charts = True)

# Iteratively generate trading signals based on maxima/minima in given window
trendy.iterlines(x, window = 30, charts = True)  # buy at green dots, sell at red dots

```

**GNU GPL v2.0 modified file notice**
__12/23/2018 - Changes made by Timothy Yu__
- Incorporated readme update for pandas_datareader import from fork
- Created `requirements.txt` (pip) and `environment.yml` (anaconda/conda) for package requirements; current code for `minitrends()` requires numpy `1.12.1` or lower to function properly without a rewrite or reimplementation of local minima/maximia detection
- `LICENSE.txt` update with original creator copyright + name as per GPL v2.0
- Added `runtests.py` with specific test and raise Exception for numpy version(s) that are not `1.12.1`
    - Behavior of masked arrays has changed above numpy `1.12.1`; minima/maxima code for minitrends() requires rewrite or reimplemention for newer numpy versions
    - Reference/dicussion about this issue on an unrelated repository/project:
    - https://github.com/dereneaton/ipyrad/issues/253#issuecomment-317842437
- Added `.pytest_cache` & `__pycache__` to `.gitignore`