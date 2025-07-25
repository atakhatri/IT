import pandas as pd

arr = [300,1200,1700,100]

ser = pd.Series(arr)

for i in range(len(ser)):
    if(ser[i] > 200):
        print(ser[i])
