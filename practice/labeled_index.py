import pandas as pd

arr = [1,2,3]
ser = pd.Series(arr,index=["one","two","three"])

print("displaying elements using minus index and labeled index : \n")
print(ser[-1])
