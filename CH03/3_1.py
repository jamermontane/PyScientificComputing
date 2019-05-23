#-*-coding:GBK -*- 


import numpy as np

from scipy.optimize import leastsq

import pylab as pl

def func(x,p):
    #����������õĺ���: A*sin(2*pi*k*x + theta)
    A,k,theta = p
    return A*np.sin(2*np.pi*k*x+theta)

def residuals(p,y,x):
    #ʵ������x,y����Ϻ���֮��Ĳ�,pΪ�����Ҫ�ҵ���ϵ��
    return y - func(x,p)

x = np.linspace(0, -2*np.pi, 100)
print("x",x)
A,k,theta = 10,0.34,np.pi/6 #��ʵ���ݵĺ�������
print("[A,k,theta]",[A,k,theta])
y0 = func(x, [A,k,theta])  #��ʵ����
print("y0",y0)
y1 = y0 + 2*np.random.randn(len(x))  #��������֮���ʵ������
print("y1",y1)
p0 = [7,0.2,0]  #��һ�β²�ĺ�����ϲ���

#����leastsq�����������
#residualsΪ�������ĺ���
#p0Ϊ��ϲ����ĳ�ʼֵ
#argsΪ��Ҫ��ϵ�ʵ������

plsq = leastsq(residuals,p0,args=(y1,x))



print("��ʵ����:",[A,k,theta])
print("��ϲ���",plsq[0]) #ʵ��������ϵĲ���

pl.rcParams['font.sans-serif'] = ['SimHei'] # ����һ���滻sans-serif���壩
pl.rcParams['axes.unicode_minus'] = False  # ���������������Ḻ���ĸ�����ʾ���⣩



pl.plot(x,y0,label="��ʵ����")
pl.plot(x,y1,label="��������ʵ������")
pl.plot(x,func(x,plsq[0]),label=u"�������")
pl.legend()
pl.show()



