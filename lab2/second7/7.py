import pandas as pd

print("\nFirst DF")
df1 = pd.DataFrame([[1,2,3,4],[5,6,7,8]],index=['r1','r2'],columns=['c1','c2','c3','c4'])
print(df1)

df2 = pd.DataFrame([[1,2,3,4],[15,16,17,18]],index=['r1','r2'],columns=['c1','c2','c3','c4'])
print("\nSecond DF")
print(df2)

new_df = pd.merge(df1,df2)
print("\nMerged DF : ")
print(new_df)