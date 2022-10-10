from pandas import Series
from envtest import my_pandas_func
import numpy as np

s = [1,3,5,np.nan,6,8]
print(my_pandas_func(s))
