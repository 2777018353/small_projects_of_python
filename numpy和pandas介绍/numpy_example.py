import numpy as np 

V = np.array([1,2,3,4,5,6,7,8,9,10])
M = np.array([[1,2,3,4,5,6,7,8,9,10],
              [10,9,8,7,6,5,4,3,2,1]])
H = np.array([[1,2,3,4,5,6,7,8,9,10],
              [10,9,8,7,6,5,4,3,2,1],
              [1,2,3,4,5,6,7,8,9,10]], dtype=complex)  #  assign type

print(V.shape, np.shape(M))
print(H.size, np.size(H))
print(V.dtype)

#  H[0, 0] = 'yanzi'  #  error!
H[0, 0] = 2  #  only change with same type
print(H)


