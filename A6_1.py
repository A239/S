'''
Author: 方凤娜
Student Number: 1619100025
Assignment：6_1
Date: 2019-4-5
Function: operation about read or write a file
'''
import random
a=[(random.random()) for i in range(50)]
a.sort()
a.reverse()

f=open(r'C:\Users\Administrator\Desktop\dasanxia\ppython\1.txt','w')
f.write(str(a))
f.close()



f=open(r'C:\Users\Administrator\Desktop\dasanxia\ppython\1.txt','r')
s=f.read()
s=eval(s)
s.reverse()

f=open(r'C:\Users\Administrator\Desktop\dasanxia\ppython\1.txt','w')
f.write(str(a))
f.write('\n')
f.write(str(s))

f.close()

f=open(r'C:\Users\Administrator\Desktop\dasanxia\ppython\1.txt','r')
s=f.read()
print(s)


