import pandas as pd

cap = ['NewDelhi','WashingtonDC','London','Paris']

ser = pd.Series(cap,index=['india','USA','UK','france'])
print("\nORIGINAL SERIES : ")
print(ser)

print("\ndisplaying elements from index 0 to 2")
print(ser[0:2])

print("\ndisplaying elements from minus indexing :")
print(ser[-1:-3:-1])


print("\ndisplaying elements from reverse order :")
print(ser[: :-1])

print("\ndisplaying elements using labeled index where end index is included : ")
print(ser['india':'UK'])
