import pandas as pd

info = [{'name':'apple','price':100,'stock':'100kgs'},
        {'name':'banana','price':60,'stock':'80kgs'},
        {'name':'dragon fruit','price':140,'stock':'110kgs'}]

print("MAIN DATAFRAME :")
df = pd.DataFrame(info,index=['f1','f2','f3'],columns=['name','price','stock'])
print(df)

print("\nwe can access column using .loc()method :")
print(df.loc[:,'name'])
print("we passed a column label to access that column along with ':'")
