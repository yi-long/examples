# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 21:17:42 2018

@author: acer
"""

'''
哥德巴赫猜想：任一大于5的数都可写为两个质数之和
'''
#核心功能函数化
def isNum(string):
    #判断是否为数值
    if string.isdigit():
        return True
    else:
        return False

def isEven(num):
    #判断是否为偶数
    if num%2==0:
        return True
    else:
        return False

def isPrime(num):
    #判断是否为质数
    if num==0 or num==1:
        flag=False
    elif num==2:
        flag=False
    else:
        for i in range(2,num):
            if num%i==0:
                flag=False
                break
            else:
                flag=True
    return flag

respone=input('请输入一个大于5的偶数：')
if isNum(respone):#判断输入是否为整数
    respone=int(respone)
    if respone>5 and isEven(respone):#判断是否为大于5的偶数
        #猜想判断
        i_list=[]
        for i in range(1,respone):
            j=respone-i#分解为两个数
            if isPrime(i) and isPrime(j):
                i_list.append(i)
                if j in i_list:
                    pass
                else:
                    print('{0}={1}+{2}'.format(respone,i,j))
    else:
        print('输入错误')
else:
    print('输入错误')