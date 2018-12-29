# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 17:53:15 2018

@author: acer
"""
'''
线性方程组的求解
'''
#SolutionofLinearEquations
import numpy as np

#def SLE(a1,a2,a3,b):
'ax**2+bx+c=0'
def STwoE(a,b,c):
    t=b**2-4*a*c
    if t>=0:
        t=np.sqrt(t)
        s1=(-b+t)/2*a
        s2=(-b-t)/2*a
        return [s1,s2]
    else:
        return ["Error"]
'''a,b,c=eval(input())
ls=STwoE(a,b,c)
print(ls)'''

'a1x^3+a2x^2+a3x+a4=0'
#SoluofsecularEquation
def SSE(ndarray):
    for i in range(len(ndarray)):
        a1,a2=[],[]
        if i%2==0:
            a1.append(ndarray[i])
        else:
            a2.append(ndarray[i])
    return a1,a2
ndarray=[1,2,3,4]
s=len(ndarray)
for i in range(s):
    a=0
    a=a+i
    a1,a2,a3,a4=[],[],[],[]
    if i%2==0:
        a3.append(i)
        a1.append(ndarray[i])
    else:
        a4.append(i)
        a2.append(ndarray[i])
print(s,a,a1,a2,a3,a4)