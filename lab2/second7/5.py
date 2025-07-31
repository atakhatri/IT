import pandas as pd

dc1 = {'name':['ata','gunjan'],
       'roll':[82,40]}

dc2 = {'name':['sunny','anubhav'],
       'roll':[48,8]}

df1 = pd.DataFrame(dc1)
print("First DF : ")
print(df1)

df2 = pd.DataFrame(dc2)
print("\nSecond DF : ")
print(df2)

new_df = df1._append(df2, ignore_index = True)
print("\nUpdated DF : ")
print(new_df)
