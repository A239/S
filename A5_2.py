'''
Author: 方凤娜
Student Number: 1619100025
Assignment：5th
Date: 2019-3-30
Version:1.0
Function: Calculate the diffierence days between two dates
'''

date1=input('Please input date1:')
date2=input('Please input date2:')
date11=date1.split('.',2)
date22=date2.split('.',2)
y1,m1,d1=date11[0],date11[1],date11[2]
y2,m2,d2=date22[0],date22[1],date22[2]

month=[1]*31+[2]*28+[3]*31+[4]*30+[5]*31+[6]*30+[7]*31+[8]*31+[9]*30+[10]*31+[11]*30+[12]*31
day=list(range(1,31+1,1))+list(range(1,28+1,1))+list(range(1,31+1,1))+list(range(1,30+1,1))+list(range(1,31+1,1))+list(range(1,30+1,1))
day=day+list(range(1,31+1,1))+list(range(1,31+1,1))+list(range(1,30+1,1))+list(range(1,31+1,1))+list(range(1,30+1,1))+list(range(1,31+1,1))

if y2<y1:
    y1,y2=y2,y1
    m1,m2=m2,m1
    d1,d2=d2,d1


for i in range(365):
    if m1==month[i] and d1==day[i]:
        for j in range(365):
            if m2==month[j] and d2==day[j]:
                difference=j-i
if difference<0:
    difference=365+difference



def leap_year(y1):
    if y1%100==0:
        if y1%400==0:
            y1=1
    else:
        if y1%4==0:
            y1=1
    return y1

ly=0
for ii in range(y1+1,y2,1):
    if leap_year(ii)==1:
        ly=ly+1

if y1==y2:
    if (((m1<=2 and d2<=28) or (m1==1)) and leap_year(y1)==1) and (((m2>=2 and d2>28) or (m2>=3)) and leap_year(y2)==1):
        difference=difference+1
else:
    if (((m1<=2 and d2<=28) or (m1==1)) and leap_year(y1)==1):
        difference=difference+1
    if (((m2>=2 and d2>28) or (m2>=3)) and leap_year(y2)==1):
        difference=difference+1

difference=difference+(y2-y1)*365+ly
print(difference)


