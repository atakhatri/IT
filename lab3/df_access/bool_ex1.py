import pandas as pd

info = [[85,22,65],
        [54,74,52],
        [48,81,59]]

print("MAIN DATAFRAME :")
df = pd.DataFrame(info,index=['maths','english','science'],columns=['st1','st2','st3'])
print(df)

print(df.loc['maths'] > 50)
