import pandas as pd

arr = [1,2,3,4,5,6,7]
index = ['one','two','three','four','five','six','seven']

ser = pd.Series(arr,index)
print("\nORIGINAL SERIES : ")
print(ser)

print("\n.head method :")
print(".head(n) returns first n elements of the series :")
print(ser.head(2))
print(".head() returns first five elements as no value is passed :")
print(ser.head())

print("\n.tail method :")
print(".tail(n) returns last n elements of the series :")
print(ser.tail(3))
print(".tail() returns last 5 elements of the series :")
print(ser.tail())

print("\n.count method :")
print(".count() returns number of NaN values in the series :")
print("count = ",ser.count())


