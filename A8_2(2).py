'''
Author: 方凤娜
Student Number: 1619100025
Assignment：8_2(2)
Date: 2019-4-5
Function: data fitting about temperature (scipy.optimize.curve_fit())
'''

import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
t_max=[17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
t_min=[-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]
t=range(0, len(t_max))

x=list(t)

# for i in range(len(x)):
#     x[i]=x[i]*30.5

x=np.round(x,5).astype('float32')  #'numpy.float64' object cannot be interpreted as an integer
y=np.round(t_min,8).astype('float32')

def residuals(A, k, theta,s, y, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return sum((y - func(x, A, k, theta,s))**2)

def func(x, A, k, theta,s):
    return -A*np.sin(2*np.pi*k*x+theta)+s 
#若不将A或S设为符号，则最低温度的绘图会很奇怪

popt, pcov = curve_fit(func, x, y)
A=popt[0]#popt里面是拟合系数，读者可以自己help其用法
k=popt[1]
theta=popt[2]
s=popt[3]
yvals=func(x,A, k, theta,s)
plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='curve_fit values')
print("全年最高温度拟合曲线："+str(-np.round(popt,2)[0]),"sin(2*pi*"+str(np.round(popt,2)[1])+'x+'+str(np.round(popt,2)[2])+')'+str(np.round(popt,2)[3]))
print("全年最高温度拟合曲线的误差平方和:",np.round(residuals(A, k, theta,s, y, x),2))



x=np.round(x,5).astype('float32')  #'numpy.float64' object cannot be interpreted as an integer
y=np.round(t_max,8).astype('float32')
popt, pcov = curve_fit(func, x, y)
A=popt[0]#popt里面是拟合系数，读者可以自己help其用法
k=popt[1]
theta=popt[2]
s=popt[3]
yvals=func(x,A, k, theta,s)
plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='curve_fit values')
print("全年最低温度拟合曲线："+str(-np.round(popt,2)[0]),"sin(2*pi*"+str(np.round(popt,2)[1])+'x+'+str(np.round(popt,2)[2])+')+'+str(np.round(popt,2)[3]))
print("全年最低温度拟合曲线的误差平方和:",np.round(residuals(A, k, theta,s, y, x),2))


plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4)#指定legend的位置,读者可以自己help它的用法
plt.title('curve_fit')

plt.show()


