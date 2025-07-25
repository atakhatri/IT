import pandas as pd

cap = pd.Series(['NewDelhi','WashingtonDC','London','Paris'],index=['india','USA','UK','france'])
print(cap[('india','UK')])
