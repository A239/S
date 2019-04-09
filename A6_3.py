'''
Author: 方凤娜
Student Number: 1619100025
Assignment：6_3
Date: 2019-4-8
Function: calculate the average value of some data
'''


import pandas as pd
data = pd.read_csv('aapl.csv')
df=data['Volume']
s=sum(df)/len(df)

ss=0
for i in range(len(df)):
    ss=ss+df[i]
ss=ss/len(df)

print(s,ss)
