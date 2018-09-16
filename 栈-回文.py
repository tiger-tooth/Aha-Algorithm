#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************


def  solve(S,T):
    zistr = [S[i:i+len(T)] for i in range(0, len(S)-len(T)+1)]
    query = {}
    [query.__setitem__(k, None) for k in T if k not in query.keys()]
    ans = []
    for ss in zistr:
        ssx = []
        [ssx.append(x) for x in ss if x not in ssx]
        if len(ssx) == len(set(T)):
            for i, k in enumerate(query.keys()):
                query[k] = ssx[i]
        else:
            continue
        new = ''.join([query[x] for x in T])
        ans.append(1) if ss==new else ans.append(0)
    return sum(ans)



    # len_T=len(T)
    # len_S=len(S)
    # for i in range(len_S-len_T):
    #     S_sub=S[i:i+len_T]
    #     sub=ord(T[0])-ord(S_sub[0])
    #     for j in range(len(S_sub)):
    #         S2.append(chr(ord(S_sub[j])+sub))
    #         #S2=S2+str(chr(S1_sub[j]+sub))
    #     if S2==T:
    #         flag=flag+1
    # return flag
    # for chr1 in S:
    #     S1.append(int(ord(chr1)))
    # for chr1 in T:
    #     T1.append(int(ord(chr1)))

    # len_T1=len(T1)
    # len_S1=len(S1)
    # for i in range(len_S1-len_T1):
    #     S1_sub=S1[i:i+len_T1]
    #     sub=T1[0]-S1_sub[0]
    #     for j in range(len(S1_sub)):
    #         S2.append(str(chr(S1_sub[j]+sub)))
    #         #S2=S2+str(chr(S1_sub[j]+sub))
    #     if S2==T:
    #         flag=flag+1
    # return flag
        


    
    # len_T1=len(T1)
    # len_S1=len(S1）

    # for i in range(len_S1-len_T1):
    #     S1_sub=S1[i:i+len_T1]
    #     for j in range(len(S1_sub)):
    #         if 
    
        


#******************************结束写代码******************************


try:
    _S = input()
except:
    _S = None

try:
    _T = input()
except:
    _T = None

  
res = solve(_S, _T)

print(str(res) + "\n")
