import pandas as pd

info = [{'name':'apple','price':100,'stock':'100kgs'},
        {'name':'banana','price':60,'stock':'80kgs'},
        {'name':'dragon fruit','price':140,'stock':'110kgs'}]

print("MAIN DATAFRAME :")
df = pd.DataFrame(info,index=['fr1','fr2','fr3'])
print(df)

print("\nwe can use .rename() method to change column labels as well,where we pass axis = 'columns'")
df = df.rename({'name':'fruit','price':'rate'},axis = 'columns')
print(df)
print("\nwe changed name and price labels with fruits and rate")
