'''
Author: 方凤娜
Student Number: 1619100025
Assignment：7_1
Date: 2019-4-5
Function: line charts of students' score
'''

import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

import numpy as np

#with open('file_path/filename.txt','a') as file:
# a = np.loadtxt('5.txt')  
# print(a) 
a=[]
with open('三9.csv', 'r') as f:
    data = f.readlines()  

    for line in data:
        odom = line.split(',')        
        #print(odom[1])

        a.append(odom)

for ii in range(1,len(a)-1):
    student_number=a[ii][0]

    x = range(15)

    y=[]
    for i in range(5,20):
        y.append(float(a[ii][i]))

    plt.figure()
    plt.plot(x, y, marker='*', mec='r', mfc='w')

    plt.yticks(np.arange(0,100,10))
    plt.xticks(np.arange(0,15),a[0][5:20])
    #print(a[0][5:20])

    plt.xlabel("考试日期") #X轴标签
    plt.ylabel("分数") #Y轴标签
    plt.title(student_number) #标题
    plt.grid()

    save_path='C:\\Users\\Administrator\\Desktop\\dasanxia\\ppython\\第七周\\三9'+"\\"+a[ii][3]+'.png'

    savefig(save_path,dpi=200)
    #注意len()和用的时候，比如a[]，之间的转换——否则会报错
    #plt.show()



