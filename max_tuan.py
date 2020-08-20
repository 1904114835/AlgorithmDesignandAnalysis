# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:56:36 2020

@author: 19041
"""

g=[ [1,1,0,1,1], 
    [1,1,1,0,1],
    [0,1,1,0,1],
    [1,0,0,1,1],
    [1,1,1,1,1]]

v=[-1 for i in range(len(g))]
result=[]
maxv=0

def is_ok(v):
    check=[]
    for i in range(len(v)):
        if v[i]==1:
            check.append(i)
    for i in range(len(check)):
        for j in range(len(check)):
            if g[check[i]][check[j]]!=1:
                return False
    return True

def bt(v):
    global maxv
    if -1 not in v:
        maxv=sum(v) if sum(v)>maxv else maxv
        if sum(v)==maxv:
            result.append([v[i] for i in range(len(v))])
        return
    if sum([1 if i==1 else 0 for i in v])+len(v)-v.index(-1)<maxv:
        return
    for choose in [0,1]:
        tempv= [v[i] if i!=v.index(-1) else choose for i in range(len(v))]
        if is_ok(tempv):
            bt(tempv)
            
bt(v)
result=[result[i]  for i in range(len(result)) if sum(result[i])==maxv]
print(result)

