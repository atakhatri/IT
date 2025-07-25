import pandas as pd

info = [{'name':'apple','price':100,'stock':'100kgs'},
        {'name':'banana','price':60,'stock':'80kgs'},
        {'name':'dragon fruit','price':140,'stock':'110kgs'}]

print("MAIN DATAFRAME :")
df = pd.DataFrame(info,index=['f1','f2','f3'],columns=['name','price','stock'])
print(df)

print("\nwe can access cols or rows using positional index using .iloc() method :")
print(df.iloc[:,0:2])
print("we passed slicing of 0 to 2 positional index to print 0th column from df")
print("\nwe can pass more than one indices to fetch more elements")
