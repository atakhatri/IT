import pandas as pd

info = [{'name':'apple','price':100,'stock':'100kgs'},
        {'name':'banana','price':60,'stock':'80kgs'},
        {'name':'dragon fruit','price':140,'stock':'110kgs'}]

print("MAIN DATAFRAME :")
df = pd.DataFrame(info,index=['fr1','fr2','fr3'])
print(df)

print("\nWE CAN DELETE ONE OR MORE ROWS FROM DF USING df.drop METHOD :")
df1 = df.drop(['fr2','fr1'],axis = 0)
print(df1)
