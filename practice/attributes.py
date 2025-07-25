import pandas as pd

arr = [1,2,3,4,5]
index=['one','two','three','four','five']

ser = pd.Series(arr,index)
print("\nORIGINAL SERIES:")
print(ser)

print("\nvisualising .name attribute :")
ser.name = 'demonstration'
print(ser)

print("\nvisualising index.name attribute :")
ser.index.name = 'Numbers'
print(ser)

print("\nvisualising VALUES,SIZE and EMPTY attributes :")
print(".VALUES returns values of the series as a list : ",ser.values)
print(".SIZE returns size of the series : ",ser.size)
print(".EMPTY returns TRUE if series is empty : ",ser.empty)

print("\nvisualising .shape attribute :")
print("shape = ",ser.shape)

print("\nvisualising .index attribute :")
print("index = ",ser.index)

print("\nvisualising .ndim attribute :")
print("dimension : ",ser.ndim)

print("\nvisualising .dtype attribute :")
print("data type : ",ser.dtype)

print("\nvisualising .nbytes attribute :")
print("bytes : ",ser.nbytes)

print("\nvisualising .hasnans attribute :")
print("has NaN values : ",ser.hasnans)


