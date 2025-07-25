import pandas as pd

arr = [1,2,3,4,5]
index = ['one','two','three','four','five']
ser = pd.Series(arr,index)

print("\nORIGINAL SERIES :")
print(ser)

print("\nusing DROP() method to delete an element :")
print("we can delete one or more elements from one drop method :")
print(ser.drop("three"))
print(ser.drop(["three","four"]))

print("\naccessing values of the series using conditions :")
print("we can use >,<,>=,<=,==,!= conditions for the values :")
print(ser[ser > 3])
print("(series[series > n]) returns values but \n(series > n) returns TRUE or FALSE ")
