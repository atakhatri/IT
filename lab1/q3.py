import pandas as pd

name = input("enter your name : ")
print(name)

ser = pd.Series(list(name))
print(ser)
