#-*-coding:GBK -*- 

import numpy as np

n = 1000000
result = np.sum(4.0/np.r_[1:n:4,-3:-n:-4])
print("result",result)

from scipy.integrate import quad
result = quad(lambda x:(1-x**2)**0.5,-1,1)[0]*2
print("result",result)

from sympy import symbols,integrate,sqrt
x = symbols("x")
print("x",x)
result = integrate(sqrt(1-x**2),(x,-1,1)) * 2
print("result",result)


import pylab as pl

x,y = np.mgrid[-2:2:500j,-2:2:500j]
z = (x**2 + y**2 - 1)**3 - x**2 * y**3
pl.contourf(x,y,z,levels=[-1,0],colors=["red"])
pl.gca().set_aspect("equal")


from mayavi import mlab
x,y,z = np.mgrid[-3:3:100j,-1:1:100j,-3:3:100j]
f = (x**2 + 9.0/4*y**2 + z**2 - 1)**3 - x**2*z**3 - 9.0/80 * y**2 * z**3
contour = mlab.contour3d(x,y,z,f,contours=[0],color=(1,0,0))
mlab.show()

import cv2
img = cv2.imread("moon.jpg",cv2.IMREAD_GRAYSCALE)
_, bimg = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
contour,_ = cv2.findContours(bimg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_TC89_L1)
contour = cv2.approxPolyDP(contour[0],epsilon=2,closed=False)
area = cv2.contourArea(contour)
perimeter = cv2.arcLength(contour,True)
result = perimeter**2/(4*area)
print("result",result)
