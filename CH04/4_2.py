#-*-coding:GBK -*- 

from sympy import *

x = Symbol("x",real=True)

print(integrate(x*sin(x),x))
print(integrate(x*sin(x),(x,0,2*pi)))


x,y,r = symbols('x,y,r')
r = symbols('r',positive=True)
circle_area = 2*integrate(sqrt(r**2-x**2),(x,-r,r))
print("circle_area",circle_area)
print(2*integrate(sqrt(r*r-x**2),(x,-r,r)))

circle_area = circle_area.subs(r,sqrt(r**2-x**2))
print("circle_area",circle_area)

print(integrate(circle_area,(x,-r,r)))