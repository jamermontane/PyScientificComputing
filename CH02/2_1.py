import numpy as np
from dask.array.tests.test_numpy_compat import dtype

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])

print("b:")
print(b)
print("c:")
print(c)
print("c.dtype:")
print(c.dtype)

print("a.shape:")
print(a.shape)
print("c.shape:")
print(c.shape)

c.shape = 4,3
print("c:")
print(c)

d = a.reshape((2,2))
print("d:")
print(d)
print("a:")
print(a)

a[1]=100
print("d:")
print(d)

e = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]],dtype = np.float)
print("e:")
print(e)

f = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]],dtype = np.complex)
print("f:")
print(f)

g = np.arange(0,1,0.1)
print("g:")
print(g)

h = np.linspace(0, 2, 20,  dtype = np.complex)
print("h:")
print(h)

i = np.logspace(0, 2, 20, dtype = np.complex)
print("i:")
print(i)

s = "123"
print("s:")
print(np.fromstring(s,dtype=np.int8))


def func(i):
    return i%4+1

print("func(10)")
print(np.fromfunction(func, (10,)))

def func2(i,j):
    return (i+1)*(j+1)

print("func2(9,9)")
print(np.fromfunction(func2,(9,9)))



a = np.arange(10)
print("a",a)
print("a[5]",a[5])
print("a[3:5]",a[3:5])
print("a[:5]",a[:5])
print("a[:-1]",a[:-1])
a[2:4]=100,101
print("a[2:4]",a[2:4])
print("a",a)
print("a[1:-1:2]",a[1:-1:2])
print("a[::-1]",a[::-1])
print("a[5:1:-2]",a[5:1:-2])

b = a[3:7]
print("b",b)
b[2]=-10
print("b",b)
print("a",a)

x = np.arange(10,1,-1)
print("x",x)
print("x[[3,3,1,8]]",x[[3,3,1,8]])
b = x[np.array([3,3,-3,8])]
b[2]=100
print("b",b)
print("x",x)
x[[3,5,1]]=-1,-2,-3
print("x",x)


x = np.arange(5,0,-1)
print("x",x)
print("x[np.array([True,False,True,False,False])]",x[np.array([True,False,True,False,False])])
print("x[[True,False,True,False,False]]",x[[True,False,True,False,False]])
#print("x[np.array([True,False,True,True])]",x[np.array([True,False,True,True])])

x = np.random.rand(10)
print("x",x)
print("x>0.5",x>0.5)
print("x[x>0.5]",x[x>0.5])



persontype = np.dtype({
    'names':['name','age','weight'],
    'formats':['S32','i','f']})
a=np.array([("Zhang",32,75.5),("Wang",24,65.2)],
           dtype=persontype)
print("a.dtype",a.dtype)
print("a[0]",a[0])
print("a[0].dtype",a[0].dtype)

c=a[1]
c["name"]="Li"
print("a",a)
print("a[0][name]",a[0]["name"])

b=a[:]["age"]
print("b",b)
b[0]=40
print("a",a)
a.tofile("test.bin")

a = np.array([[0,1,2],[3,4,5],[6,7,8]],dtype=np.float32)
print("a",a)
print("a.strides",a.strides)
