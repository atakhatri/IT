import pandas as pd

info = ['Ata','Gunjan','Anubhav']

ser = pd.Series(info)
print(ser)

print("\nseries in upper case:\n",ser.str.upper())
print("\nseries in lower case:\n",ser.str.lower())

print("\nsize of every string in the series :\n",ser.str.len())
