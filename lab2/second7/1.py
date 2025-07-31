import pandas as pd
import numpy as np

info = {'one':[11,22,33],'two':[44,55,66],'three':[77,88,99]}

df = pd.DataFrame(info)
print(df)

print("\ndefault index = ",df.index)
df.index = df['one']
print("\n",df)

print("\nnew index = ",df.index)
