import pandas as pd

val = [25000,12000,8000,5000]

ser = pd.Series(val)
print("Original Series: \n")
print(ser)

ser[3] = 7000
print("Modified Series: \n")
print(ser)

