#-*-coding:GBK -*- 

from sympy import *

print(E**(I*pi)+1)


x = Symbol('x')
print(expand(E**(I*x),complex=true))

x = Symbol("x",real = True)

print(expand(exp(I*x),complex=True))

tmp = series(exp(I*x),x,0,10)
pprint(tmp)

pprint(re(tmp))

pprint(series(cos(x),x,0,10))

pprint(im(tmp))

pprint(series(sin(x),x,0,10))