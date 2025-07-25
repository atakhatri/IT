import pandas as pd

info = [{'name':'apple','price':100,'stock':'100kgs'},
        {'name':'banana','price':60,'stock':'80kgs'},
        {'name':'dragon fruit','price':140,'stock':'110kgs'}]

print("MAIN DATAFRAME :")
df = pd.DataFrame(info,index=[1,2,3])
print(df)

print("\nDATAFRAME AFTER ADDING ONE COLUMN OF SALES : ")
df['sales'] = ['94kgs','66kgs','109kgs']
print(df)
#if we add a column with lesser values than the number of rows in the main df then it results in a valueerror
