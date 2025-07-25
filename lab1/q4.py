import pandas as pd

D={'Jan':31, 'Feb':28, 'March':31,
   'April':30, 'May':31, 'June':30,
   'July':31, 'Aug':31, 'Sep':30,
   'Oct':31, 'Nov':30, 'Dec':31}

ser = pd.Series(D)
print(ser)
