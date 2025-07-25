import pandas as pd

arr = [1,2,3,4]
ser = pd.Series(arr,index=['one','two','three','four'])

print("\nORIGINAL SERIES : ")
print(ser)

ser[1:3] = 22
print("\nseries after modifying elements on index ONE to THREE : ")
print(ser)

ser['two':'four'] = 20
print("\nseries after modifying elements on index ONE to FOUR using labeled index : ")
print(ser)

