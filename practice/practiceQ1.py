import pandas as pd

arr = [1,2,3,4,5]
ser = pd.Series(arr,index=['one','two','three','four','five'])

print("\nORIGINAL SERIES : ")
print(ser)

print("\nA:")
print(ser['two'])

print("\nB:")
print(ser[2])

print("\nC:")
print(ser[0])

print("\nD:")
print(ser[0:2])

print("\nE:")
print(ser['two':'three'])

print("\nF:")
print(ser[::-1])

print("\nG:")
print(ser[1:4])

print("\nH:")
print(ser[["two","four"]])

print("\nI:")
print(ser['two':'four'])

print("\nJ:")
print(ser[-1])
