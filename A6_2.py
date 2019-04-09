'''
Author: 方凤娜
Student Number: 1619100025
Assignment：6_2
Date: 2019-4-6
Function: record score and age of students
'''

import pandas as pd

#任意的多组列表
no = [1,2,3,4,5]
name = ['mayi','jack','tom','rain','hanmeimei']    
age = [18,21,25,19,23]
score = [99,89,95,80,81]

#字典中的key值即为csv中列名

columns=['No.','Name','Age','Score']
dataframe = pd.DataFrame({'No.':no,'Name':name,'Age':age,'Score':score})

#将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("test.csv",index=False,columns=columns,sep=',')
