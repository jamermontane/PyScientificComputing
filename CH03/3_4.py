#-*-coding:GBK -*- 

import numpy as np
import pylab as pl
from scipy import interpolate

x = np.linspace(0, 2*np.pi+np.pi/4, 10)
print("x",x)
y = np.sin(x)
print("y",y)

x_new = np.linspace(0, 2*np.pi+np.pi/4, 100)
print("x_new",x_new)
f_linear = interpolate.interp1d(x,y)
tck = interpolate.splrep(x,y)
y_bspline = interpolate.splev(x_new, tck)


pl.rcParams['font.sans-serif'] = ['SimHei'] # ����һ���滻sans-serif���壩
pl.rcParams['axes.unicode_minus'] = False  # ���������������Ḻ���ĸ�����ʾ���⣩

pl.plot(x,y,"o",label="ԭʼ����")
pl.plot(x_new,f_linear(x_new),label="���Բ�ֵ")
pl.plot(x_new,y_bspline,label="B-spline��ֵ")
pl.legend()
pl.show()


