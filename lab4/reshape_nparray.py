import numpy as np

nparr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(nparr)

shape = (6,2)
n_nparr = np.reshape(nparr, shape)
print(n_nparr)