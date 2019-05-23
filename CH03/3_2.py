#-*-coding:GBK -*- 
#�������ø���fmin����������������

import scipy.optimize as opt
import numpy as np

def test_fmin_convolve(fminfunc,x,h,y,yn,x0):
    #x(*)h=y,(*)��ʾ���
    #ynΪ��y�Ļ��������һЩ���������Ľ��x0Ϊ���x�ĳ�ʼֵ
    
    def convolve_func(h):
        #����yn-x(*)h��power
        #fmin��ͨ������ʹ�ô�power��С"""
        return np.sum((yn-np.convolve(x,h))**2)
    
    #����fmin��������x0Ϊ��ʼֵ
    h0 = fminfunc(convolve_func,x0)
    
    print(fminfunc.__name__)
    print("----------------------------")
    #���x(*)h0��y֮���������
    print("error of y:",np.sum((np.convolve(x,h0)-y)**2)/np.sum(y**2))
    #���h0��h֮���������
    print("error of h:",np.sum((h0-h)**2)/np.sum(h**2))
    print("")
    
def test_n(m,n,nscale):
    #�������x,h,y,yn,x0�����У����ø���fmin�������b mΪx�ĳ���,nΪh�ĳ���,nscaleΪ���ŵ�ǿ��
    
    x = np.random.randn(m)
    h = np.random.randn(n)
    y = np.convolve(x,h)
    yn = y + np.random.rand(len(y))*nscale
    x0 = np.random.rand(n)
    
    test_fmin_convolve(opt.fmin, x, h, y, yn, x0)
    test_fmin_convolve(opt.fmin_powell, x, h, y, yn, x0)
    test_fmin_convolve(opt.fmin_cg, x, h, y, yn, x0)
    test_fmin_convolve(opt.fmin_bfgs, x, h, y, yn, x0)
    
if __name__ == "__main__":
    test_n(200, 20, 0.1)
    
    
    
    
    
        