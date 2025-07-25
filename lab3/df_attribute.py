import pandas as pd

info = [[85,22,65,76],
        [54,74,52,67],
        [48,81,59,34],
        [85,22,65,65]]

print("MAIN DATAFRAME :")
df = pd.DataFrame(info,index=['math','sci','eng','comp'],columns=['st1','st2','st3','st4'])
print(df)

print("\n",df.index)#returns row labels
print("\n",df.columns)#returns col labels
print("\n",df.dtypes)#returns dtype of columns
print("\n",df.shape)#returns dimensions
print("\n",df.size)#returns num. of total elements m x n
print("\n",df.T)#returns transpose of df
print("\n",df.values)#returns only values in form of array
print("\n",df.empty)#returns True of df is empty
