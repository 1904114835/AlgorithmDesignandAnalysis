# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 00:46:09 2020

@author: 19041
"""

v=[45,25,25]
w=[16,15,15]
sumw=30
way=[-1 for i in range(len(v))]
result=[[],0]

times=0
def bt(way,now):
    global times
    times+=1
    if now==len(way):
        global result
        t=sum([v[i]  if way[i]>0 else 0 for i in range(len(v))])
        if t>result[-1]:
            result=[[way[i] for i in range(len(way)) ],t]
        return
    for choose in [0,1]:
        if sumw-sum([w[i] if way[i]>0 else 0 for i in range(len(v))])>=w[now]*choose:
            bt([way[i] if i!=now else choose for i in range(len(way))],now+1)
bt(way,0)
print("遍历次数",times)
print(result)