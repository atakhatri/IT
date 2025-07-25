import pandas as pd

info = [{'name':'apple','price':100,'stock':'100kgs'},
        {'name':'banana','price':60,'stock':'80kgs'},
        {'name':'dragon fruit','price':140,'stock':'110kgs'}]

print("MAIN DATAFRAME :")
df = pd.DataFrame(info,index=['fr1','fr2','fr3'])
print(df)

print("\nwe can use .rename() method to change one or more row labels in the df :")
df = df.rename({'fr1':'first','fr2':'second','fr3':'third'},axis = 'index')
print(df)
#we can pass axis = 'index',it specifies that we intend to change labels at row indices,we can skip this as method bydefault takes row index for replacement
