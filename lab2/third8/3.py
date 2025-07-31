import pandas as pd

data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]

df = pd.DataFrame(data)
print(df)

print("\nFirst 3 rows from the DF : ")
print(df.head(3))