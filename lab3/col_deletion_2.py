import pandas as pd

info = [{'name':'apple','price':100,'stock':'100kgs'},
        {'name':'banana','price':60,'stock':'80kgs'},
        {'name':'dragon fruit','price':140,'stock':'110kgs'}]

print("MAIN DATAFRAME :")
df = pd.DataFrame(info,index=['fr1','fr2','fr3'])
print(df)

print("\nwe can use .drop() method to remove one or more columns :")
df1 = df
print(df1.drop(['price','stock'],axis = 1))
print("\nremoved column : price and stock")
