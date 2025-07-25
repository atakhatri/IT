import pandas as pd

info = [{'name':'apple','price':100,'stock':'100kgs'},
        {'name':'banana','price':60,'stock':'80kgs'},
        {'name':'dragon fruit','price':140,'stock':'110kgs'}]

print("MAIN DATAFRAME :")
df = pd.DataFrame(info,index=['f1','f2','f3'])
print(df)

print("\nwe can access elements using label based indexing from df\nwe use .loc() method to do so :")
print(df.loc[['f1','f2']])
print("we passed two row indices to access those rows")
