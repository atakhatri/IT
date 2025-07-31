import pandas as pd

info = ['Ata Khatri','Gunjan Manek','Anubhav Singh']

ser = pd.Series(info)
print(ser)

print("\nRemoving all whitespaces : ")
print(ser.str.strip())

print("\nRemoving left whitespaces : ")
print(ser.str.lstrip())

print("\nRemoving right whitespaces : ")
print(ser.str.rstrip())