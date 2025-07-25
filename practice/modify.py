import pandas as pd

arr = [1,2,3,4]

ser = pd.Series(arr,index=['one','two','three','four'])

print("\nORIGINAL SERIES : ")
print(ser)

ser['two'] = 5
print("\nafter modifying element at index TWO :")
print(ser)

