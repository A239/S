'''
Author: 方凤娜
Student Number: 1619100025
Assignment：5th
Date: 2019-3-30
Version:1.0
Function: A management system address book 
'''
n=0
while(n<7):
    sys=[[1,'STUO1',123456],[2,'STUO2',456789]]
    print('1.新增联系人')
    print('2.删除联系人')
    print('3.修改手机号码')
    print('4.修改联系人')
    print('5.查询联系人')
    print('6.显示所有联系人')
    print('7.退出')
    n=int(input("Please input a number:"))

    # 1.新增联系人. (重名)
    if n==1:
        name=input('Please input a name:')
        ii=0
        for i in range(len(sys)):
            if name in sys[i]:
                ii+=1
                

        if ii!=0:
            while(name!='0' or ii!=0):
                name=input('The name is existent in this menu. Please input another name (to exit, please input 0):')
                n=0
                ii=0
                for i in range(len(sys)):
                    if name in sys[i]:
                        print('The name exists in this menu. Please input another name:')
                        ii+=1
        
        else:
            phone_number=input('Please input a phone number:')
            sys.append([len(sys)+1,name,phone_number])
            print('The new menu:')
            for i in range(len(sys)):
                print(sys[i]) \


    # 2.删除联系人 
    if n==2:
        print(sys)
        delete_choice=int(input('Please input a number about the name you want to delete:'))
        sys.remove(sys[delete_choice-1])
        for i in range(len(sys)):
            sys[i][0]=i+1
        print('The new menu:')
        print(sys)


    # 3.修改手机
    if n==3:
        print(sys)
        modify=int(input('Please input a number about the phone number you want to modify:'))
        phone_number=input('Please input a new phone number:')
        sys[modify-1][2]=phone_number
        print('The new menu:')
        print(sys)

    # 4.修改联系人姓名
    if n==4:
        name=input('Please input the name you want to modify (to exit, please input 0):')
        ii,iii=1,1
        while(ii>0 and name!='0'):
            for i in range(len(sys)):
                if name in sys[i]:
                    ii=0
                    new_name=input('Please input a new name (to exit, please input 0):')
                    
                    while(iii>0 and name!='0'):
                        for i1 in range(len(sys)):
                            if new_name in sys[i1]: 
                                iii+=1
                                new_name=input('The new name is existent. Please input another name(to exit, please input 0):')
                                
                            else:
                                iii=0
                                ii=0
                                sys[i][1]=new_name
                
            if ii>0:
                name=input('The name is not-existent in this menu. Please check your input again (to exit, please input 0):')
        if name!='0' and new_name!='0':    
            print(sys)
        else:
            n=7

    # 5.查询联系人
    if n==5:
        name=(input('Please input a name you seek (to exit, please input 0):'))
        ii=0
        while(ii==0 and name!='0'):
            for i in range(len(sys)):
                if name==sys[i][1]:
                    ii=1
                    print('Check result:')
                    print(sys[i][1],sys[i][2])
                    print()

            if ii==0:
                print('Sorry, the name is non-exist in this menu. Please check your spelling.')
                name=(input('Please input a name you seek(to exit, please input 0):'))
        if name=='0':
            n=7

            


    # 6.显示所有联系人
    if n==6:
        for i in range(len(sys)):
            print(i+1,sys[i][1])
        print()
