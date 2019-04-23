'''
Author: 方凤娜
Student Number: 1619100025
Assignment：8_1
Date: 2019-4-21
Function:  experimental data fitting
'''

import numpy as np
from scipy.optimize import leastsq
import pylab as pl

x=[ 0,	3,	6,	9,	12,	15,	18,	21,	24,	27,	30,	33,	36,	39,	42,	45,	48]
for i in range(len(x)):
    x[i]=x[i]*np.pi/180
#x[i]=round(x[i],3)
x=np.round(x,5).astype('float32')
y0=[48.5,52.6,27.0,-13.8,-38.0,-29.5,-4.9,25.2,48.6, 53.2,26.7,-16.1,-39.4,-29.9,-3.5,25.2,48.5]
y0=np.round(y0,5).astype('float32')
#print(x,y0)


def func(x, p):
    """
    数据拟合所用的函数: A*sin(2*pi*k*x + theta)
    """
    A, k, theta = p
    return A*np.sin(2*np.pi*k*x+theta)   

def residuals(p, y, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y - func(x, p)

#x = np.linspace(0, -2*np.pi, 100)
#A, k, theta = 10, 0.34, np.pi/6 # 真实数据的函数参数
#y0 = func(x, [A, k, theta]) # 真实数据
#y1 = y0 + 2 * np.random.randn(len(x)) # 加入噪声之后的实验数据    

p0 = [48, 2.5, 0.1] # 第一次猜测的函数拟合参数

# 调用leastsq进行数据拟合
# residuals为计算误差的函数
# p0为拟合参数的初始值
# args为需要拟合的实验数据
plsq = leastsq(residuals, p0, args=(y0, x))



pl.rcParams['font.family'] = ['simHei']
pl.rcParams['font.sans-serif'] = ['simHei'] # 步骤一（替换sans-serif字体）
pl.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）

pl.plot(x, y0, label=u"真实数据")
x1 = np.linspace(0, 0.8, 100)
pl.plot(x1, func(x1, plsq[0]), label=u"拟合的曲线")

pl.plot(x, func(x, plsq[0]), label=u"拟合数据")
pl.legend()
pl.show()
#数据少，拟合不够好