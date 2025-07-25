import pandas as pd

#demonstration to create DataFrame using nested list with appropriate column heading and row index

mat = [['ata',82,19],
       ['gunjan',40,19],
       ['sunny',48,20]]
df = pd.DataFrame(mat,index=[1,2,3],columns=['name','roll','age'])
print(df)
