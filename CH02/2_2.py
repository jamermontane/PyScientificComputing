import numpy as np


x = np.linspace(0,2*np.pi,10)
print("x",x)

y = np.sin(x)
print("y",y)

t = np.sin(x,x)
print("x",x)

print("id(x)==id(x)",id(x)==id(x))
print("id(x)==id(y)",id(x)==id(y))

import time
import math

x = [i*0.001 for i in xrange(1000000)]
start = time.clock()
for i,t in enumerate(x):
    x[i] = math.sin(t)
print("math.sin:",time.clock()-start)

x = [i*0.001 for i in xrange(1000000)]
x = np.array(x)
start = time.clock()
np.sin(x,x)
print("numpy.sin:",time.clock()-start)    

x = [i*0.001 for i in xrange(1000000)]
start = time.clock()
for i,t in enumerate(x):
    x[i] = np.sin(t)
print("numpy.sin loop:",time.clock()-start)

def triangle_wave(x,c,c0,hc):
    x = x-int(x)
    if x>c : r=0.0
    elif x<c0: r = x/c0 * hc
    else: r =(c-x) /(c-c0)*hc
    return r


x = np.linspace(0,2,1000)
y = np.array([triangle_wave(t, 0.6, 0.4, 1.0) for t in x])


triangle_ufunc = np.frompyfunc(lambda x: triangle_wave(x, 0.6, 0.4, 1.0),1,1)
y2 = triangle_ufunc(x)

def triangle_func(c,c0,hc):
    def trifunc(x):
        x = x-int(x)
        if x>c : r=0.0
        elif x<c0: r = x/c0 * hc
        else: r =(c-x) /(c-c0)*hc
        return r
    return np.frompyfunc(trifunc,1,1)

y2 = triangle_func(0.6, 0.4, 1.0)(x)
    
    
a = np.arange(0,60,10).reshape(-1,1)
print("a",a) 
print("a.shape",a.shape)  
b=np.arange(0,5)
print("b",b)
print("b.shape",b.shape) 
c = a + b
print("c",c)
print("c.shape",c.shape)
print("b",b)
b.shape=1,5
print("b",b)
b = b.repeat(6,axis=0)
print("b",b)
a = a.repeat(5,axis=1)
print("a",a)

x,y = np.ogrid[0:5,0:5]
print("x",x)
print("y",y)

x,y = np.ogrid[0:1:4j,0:1:3j]
print("x",x)
print("y",y)


#from enthought.mayavi import mlab

# 
# x,y = np.ogrid[-2:2:20j,-2:2:20j]
# z = x * np.exp(-x**2 - y**2)
# 
# pl = mlab.surf(x,y,z,warp_scale="auto")
# mlab.axes(xlable='x',ylabel='y',zlabel='z')
# mlab.outline(pl)



print(np.add.reduce([1,2,3]))
print(np.add.reduce([[1,2,3],[4,5,6]],axis=1))
print(np.add.accumulate([1,2,3]))        
print(np.add.accumulate([[1,2,3],[4,5,6]],axis=1))        

a = np.array([1,2,3,4])
print("a",a)
result = np.add.reduceat(a,indices=[0,1,0,2,0,3,0])
print("result",result)
