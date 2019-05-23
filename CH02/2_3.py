import numpy as np

a = np.matrix([[1,2,3],[5,5,6],[7,9,9]])
print("a*a**-1",a*a**-1)

a = np.array([1,2,3])
print("a",a)
a=a.reshape((-1,1))
print("a",a)
a=a.reshape((1,-1))
print("a",a)


a = np.arange(12).reshape(2,3,2)
b = np.arange(12,24).reshape(2,2,3)
c = np.dot(a,b)

print("a",a)
print("b",b)
print("c",c)

print(np.alltrue(c[0,:,0,:] == np.dot(a[0],b[0])))
print(np.alltrue(c[1,:,0,:]==np.dot(a[1],b[0])))
print(np.alltrue(c[0,:,1,:]==np.dot(a[0],b[1])))
print(np.alltrue(c[1,:,1,:]==np.dot(a[1],b[1])))

a = np.arange(12).reshape(2,3,2)
b = np.arange(12,24).reshape(2,3,2)
c = np.inner(a,b)
c = c.shape
print("c",c)

c = np.outer([1,2,3], [4,5,6,7])
print("c",c)

a = np.random.rand(10,10)
b = np.random.rand(10)
x = np.linalg.solve(a, b)
print("a",a)
print("b",b)
print("x",x)
print(np.sum(np.abs(np.dot(a,x) - b )))
