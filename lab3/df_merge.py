import pandas as pd

info = [[85,22,65,76],
        [54,74,52,67],
        [48,81,59,34],
        [85,22,65,65],
        [54,74,52,55],
        [48,81,59,21]]

info1 =[[77,52,35,98],
        [94,34,82,77],
        [44,61,50,55],
        [77,52,35,91],
        [44,61,50,55],
        [77,52,35,91]]

print("MAIN DATAFRAME :")
df = pd.DataFrame(info,index=[1,2,3,4,5,6],columns=['st1','st2','st3','st4'])
print(df)

print("\nSECOND DATAFRAME :")
df1 = pd.DataFrame(info1,index=[1,2,3,4,5,6],columns=['st1','st2','st3','st4'])
print(df1)

print("\nNEW DATAFRAME :")
df = df._append(df1,sort=True)
print(df)
