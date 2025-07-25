import pandas as pd
import numpy as np

print("creation of dataframe using numpy arrays and giving proper row and column index")
ar1 = np.array([1,2,3,4,5])
ar2 = np.array([11,22,33,44,55])
ar3 = np.array([111,222,333,444,555])

df = pd.DataFrame((ar1,ar2,ar3),index=['ones','tens','hundreds'],columns=['a','b','c','d','e'])
print(df)
