#-*-coding:GBK -*- 

import numpy as np


def half_circle(x):
    return (1-x**2)**0.5


N = 10000
x = np.linspace(-1,1,N)
print("x",x)
dx = 2.0/N
print("dx",dx)
y = half_circle(x)
print("y",y)
result = dx * np.sum(y[:-1]+y[1:])
print("result",result)

print(y[:-1])
print(y[1:])

result = np.trapz(y, x) * 2

print("result",result)


from scipy import integrate

pl_half,err = integrate.quad(half_circle,-1,1)
print("pl_half*2",pl_half*2)


def half_sphere(x,y):
    return (1-x**2-y**2)**0.5

result = integrate.dblquad(half_sphere,-1,1,
                           lambda x:-half_circle(x),
                           lambda x:half_circle(x))
print("result",result)
print(np.pi*4/3/2)