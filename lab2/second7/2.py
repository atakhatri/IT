import pandas as pd
import numpy as np

info = {'one':[11,22,33],'two':[44,55,66],'three':[77,88,99]}
labels = [1,2,3]
df = pd.DataFrame(info,index = labels)
print("df with int indices : ")
print(df)

labels2 = [1.0,1.1,1.2]
df2 = pd.DataFrame(info,index = labels2)
print("\ndf with float indices : ")
print(df2)


