import pandas as pd

print("demonstration of creation of dictionary using multiple series(1d array) and proper row and column index")
s1 = pd.Series([1,11,111])
s2 = pd.Series([2,22,222])
s3 = pd.Series([3,333])

df = pd.DataFrame([s1,s2,s3],index=['r1','r2','r3'],columns=[1,2,3])
print(df)
#if a val in a series is missing NaN val is shown in that corresponding column
