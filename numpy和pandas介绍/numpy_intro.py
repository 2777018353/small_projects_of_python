import numpy as np 

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

b = a[:2, 1:3]  #  slide
b[0,0] = 88  #  same as pointer

print(a)
print(b)

c = np.zeros((2, 20))
print(c)
d = np.ones((20, 5))
print(d)
e = np.full((5, 7), 8)
print(e)

f = np.eye(10)  #  identity matrix(short with I, I listens like eye)
print(f)

g = np.random.rand(2, 3)
print(g)

h = np.array([[1,2],[3,4],[5,6]])
i = np.array([h[0,1], h[1,1], h[2,0]])
i[[0, 0]] = 8
print(h)
print(i)
j = h[[0,1,2], [0,1,0]]

k = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
l = np.array([0,2,0,1])
m = k[np.arange(4), l]
print(np.arange(4))
print(k)
print(m)

k[np.arange(4), l] += 100
print(k)

n = np.array([[1,2,3],[4,5,6],[7,8,9]])
boolean_array_indexing = (n > 5)  #  turn to bool
print(boolean_array_indexing)
print(n > 4)

x = np.array([[1,2], [3,4]], dtype=float)
y = np.array([[5,6], [7,8]], dtype=float)
print(x + y, '\n', np.subtract(x, y), '\n', np.multiply(x, y), '\n', np.divide(x, y), '\n', np.sqrt(x))

print(x.dot(y), '\n', np.dot(x, y))

z = np.array([[1,2], [3,4]])
print(np.sum(z))  #  sum all elements
print(np.sum(z, axis=1))
print(z.T)  #  transpose

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
y = np.array([1,0,1])
print(x + y)  #  bordcasting

z = np.zeros_like(x)
print(z)

for i in range(4):  #  like bordcasting
    z[i, :] = x[i, :] + y
print(z)