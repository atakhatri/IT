import pandas as pd

info = [{'name':'apple','price':100,'stock':'100kgs'},
        {'name':'banana','price':60,'stock':'80kgs'},
        {'name':'dragon fruit','price':140,'stock':'110kgs'}]

print("MAIN DATAFRAME :")
df = pd.DataFrame(info,index=['fr1','fr2','fr3'])
print(df)

print("\nwe can use .pop() method to remove a column and also return that col value :")
df1 = df
print("deleted column : stock \n",df1.pop('stock'))
print("REMAINING DATAFRAME :")
print(df1)
