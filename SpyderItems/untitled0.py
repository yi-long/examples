# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:56:36 2018

@author: acer
"""

import numpy as np

def solve2(a,b,c):
    _delt=b**2-4*a*c
    s1=(-b+np.sqrt(_delt))/(2*a)
    s2=(-b-np.sqrt(_delt))/(2*a)
    return s1,s2

#def SLE(a1,a2,a3,b):
'ax**2+bx+c=0'
def STwoE(a,b,c):
    t=b**2-4*a*c
    if t>=0:
        t=np.sqrt(t)
        s1=(-b+t)/(2*a)
        s2=(-b-t)/(2*a)
        return [s1,s2]
    else:
        return ["Error"]
'''
数据的获取方式（输入方式）
数据的返回形式
'''
a,b,c=3,10,4
ls=STwoE(a,b,c)
lt=solve2(a,b,c)
print(ls,lt)