# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:26:33 2020

@author: 19041
"""

n=4

queen=[]
result=[]
def is_ok(queen,choose):
    if len(queen)==0:
        return True
    for i in range(len(queen)):
        if queen[i]==choose:
            return False
        if abs(i-len(queen))==abs(queen[i]-choose):
            return False
    return True
def draw(queen):
    for i in range(n):
        for j in range(n):
            if j==queen[i]:
                print('X',end=' ')
            else:
                print('.',end=' ')
        print()
    print()
    
def bt(queen,chooses,ceng):
    if ceng==n:
        result.append(queen)
        draw(queen)
        return
    for choose in chooses:
        if is_ok(queen,choose):
            t=[i for i in queen]
            t.append(choose)
            bt(t,[i for i in chooses if i!=choose],ceng+1)

chooses=[i for i in range(n)]
bt(queen,chooses,0)
print(len(result))







