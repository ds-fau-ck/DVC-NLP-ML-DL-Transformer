import numpy as np 
from scipy.sparse import csr_matrix
A=np.array([
    [1,0,0,0,0,1,0],
    [0,1,0,0,0,3,0],
    [0,0,0,0,1,0,0],
    ])
print(A)

c=csr_matrix(A)
print(c)
print(type(c))
B=c.todense()
print(B)