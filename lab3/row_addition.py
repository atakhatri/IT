import pandas as pd

info = [{'name':'apple','price':100,'stock':'100kgs'},
        {'name':'banana','price':60,'stock':'80kgs'},
        {'name':'dragon fruit','price':140,'stock':'110kgs'}]

print("MAIN DATAFRAME :")
df = pd.DataFrame(info,index=['fr1','fr2','fr3'])
print(df)

print("\nDATAFRAME AFTER ADDING A NEW ROW FOR 4TH FRUIT :")
df.loc['fr4'] = ['strawberry',85,'77kgs']
print(df)
#if we add a new row with lesser values then the number of columns then it results in a value-error
