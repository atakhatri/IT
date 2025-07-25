import pandas as pd

arr = [1,11,111]

ser = pd.Series(arr)
print("\nORIGINAL SERIES : ")
print(ser)

print("\nADDING something to the series :")
print(ser + 11)

print("\nMULTIPLYING something to the series : ")
print(ser * 3)

arr2 = [2,22,222]
ser2 = pd.Series(arr2)
print("\nSECOND SERIES :")
print(ser2)dd

print("\nadding two series : ")
print(ser + ser2)


