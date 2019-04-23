'''
Author: 方凤娜
Student Number: 1619100025
Assignment：8_2
Date: 2019-4-22
Function: data fitting about temperature (leastsq)
'''


import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import leastsq
import pylab as pl

plt.rcParams['axes.unicode_minus']=False

t_max=[17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
t_min=[-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]
t=range(0, len(t_max))
#t=np.linspace(0,365, len(t_max))
x=list(t)
x=np.round(x,5).astype('float32')  #'numpy.float64' object cannot be interpreted as an integer

def func(x, p):
    A, k, theta,s = p      #s是上下移动
    return A*np.sin(2*np.pi*k*x+theta)+s  

def func2(y0):

    y0=np.round(y0,5).astype('float32')

    def residuals(p, y, x):
        """
        实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
        """
        return y - func(x, p)

    p0 = [50, 0.05, 0.1,-40] # 第一次猜测的函数拟合参数

    plsq = leastsq(residuals, p0, args=(y0, x))
    return plsq[0]


plt.rcParams['font.family'] = ['simHei']
plt.rcParams['font.sans-serif'] = ['simHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）

plt.plot(x, t_min, label=u"真实数据")
plt.plot(x, func(x, func2(t_min)), label=u"拟合数据")

plt.plot(x, t_max, label=u"真实数据")
plt.plot(x, func(x, func2(t_max)), label=u"拟合数据")
plt.xticks(x,np.arange(0,365,int(365/len(x))))
plt.legend()
plt.show()






