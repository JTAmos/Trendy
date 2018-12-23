#### **GNU GPL v2.0 modified file notice** ###
# 12/23/2018 - Changes made by Timothy Yu
	# runtests.py created for numpy 1.12.1 version check

import pytest
import numpy as np

print(np.__version__)
#np.show_config())
if str(np.__version__) != '1.12.1':
	raise Exception('Numpy version is NOT 1.12.1; minitrends maxima/minima may not work!')
