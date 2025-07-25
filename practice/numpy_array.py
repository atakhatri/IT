import numpy as np
import pandas as pd

ar = np.array([1,2,3])
ser = pd.Series(ar,index=['a','b','c'])
print(ser)
