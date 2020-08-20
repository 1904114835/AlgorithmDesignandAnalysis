# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:07:25 2020

@author: 19041
"""

import copy
a=[1,2,3,4,5]
print(a.index(1))
b=copy.deepcopy(a)
for i in b:
    b.remove(i)
    print(b,i)
print('a',a)
print('b',b)
