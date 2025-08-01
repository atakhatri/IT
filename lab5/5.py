import numpy as np

arr = [0,1,2,3,4,5,6,7,8,9]
nparr = np.array(arr)
print(nparr)

nparr[nparr] = -1
print(nparr)