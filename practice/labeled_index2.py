import pandas as pd

cap = ['NewDelhi','WashingtonDC','London','Paris']

ser = pd.Series(cap,index=['india','USA','UK','france'])

print("displaying element using labeled index : \n")
print(ser['india'])

print("displaying element using positional index : \n")
print(ser[2])
