# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:36:26 2020

@author: 19041
"""

g=[[0,1,1],
   [1,0,1],
   [1,1,0]]

g=[ [0,1,0,1,1], 
    [1,0,1,0,1],
    [0,1,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,0]]
v=[-1 for i in range(len(g))]
result=[]
maxv=0

def is_ok(v):
    if -1 not in v:
        now=len(v)-1
    else:        
        now=v.index(-1)-1
    for i in range(len(g)):
        if g[now][i]==1:
            if v[i]==v[now]:
                return False
    return True

def bt(v):
    if -1 not in v:
        result.append([v[i] for i in range(len(v))])
        return
    for choose in [0,1,2]:
        tempv= [v[i] if i!=v.index(-1) else choose for i in range(len(v))]
        if is_ok(tempv):
            bt(tempv)
            
bt(v)
print(result)

