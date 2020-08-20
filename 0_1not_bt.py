# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 01:47:27 2020

@author: 19041
"""

v=[45,25,25]
w=[16,15,15]
sumw=30
way=[-1 for i in range(len(v))]
chooses=[0,1]

def choose_node(nodes):
    temp=[nodes[i].index(-1) for i in range(len(nodes))]
    up=temp.index(min(temp))
    return [nodes[up][i] for i in range(len(nodes[up]))]

def get_new_node(now_node,choose):
    return [now_node[i] if i!=now_node.index(-1) else choose for i in range(len(now_node))]

def is_ok(new_node,result,sv):
    if len(result)==0:
        return True
    if sum([w[i] if new_node[i]>0 else 0 for i in range(len(v))])<=sumw:
        future=0
        if -1 not in new_node:
            pass
        else:
            future=sum([sv[i] for i in range(len(v)-new_node.index(-1)-1)])
        future_max=sum([v[i]  if new_node[i]>0 else 0 for i in range(len(v))])+future
        if sum([v[i]  if result[i]>0 else 0 for i in range(len(v))])<future_max:
            return True
    return False
    
def is_end(new_node):
    if -1 not in new_node:
        return True
    else:
        return False
    
def is_better(new_node,result):
    if len(result)==0:
        return True
    if sum([v[i]  if new_node[i]>0 else 0 for i in range(len(v))])>\
        sum([v[i]  if result[i]>0 else 0 for i in range(len(v))]):
        return True
    else:
        return False
    
def bfs(nodes):
    result=[]
    sv=sorted(v)
    times=0
    while len(nodes)!=0:
        times+=1
        now_node=choose_node(nodes)
        nodes.remove(now_node)
        for choose in chooses:
            new_node=get_new_node(now_node,choose)
            if is_ok(new_node,result,sv):
                if is_end(new_node):
                    if is_better(new_node,result):
                        result=new_node
                else:                    
                    nodes.append(new_node)
    print("遍历次数",times)
    return result

nodes=[way]       
result=bfs(nodes)
print("result",result)
