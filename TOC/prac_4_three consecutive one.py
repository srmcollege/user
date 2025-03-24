# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 12:32:32 2025

@author: INDIA
"""

m=[]
def state_q0(n):
    m.append("q0")
    print("state q0")
    
    if(len(n)==0):
        print("string is not accepted")
    else:
        if(n[0]=='0'):
            state_q0(n[1:])
        elif(n[0]=='1'):
            state_q1(n[1:])
            
def state_q1(n):
    m.append("q1")
    print("state q1")
    
    if(len(n)==0):
        print("string is not accepted")
    else:
        if(n[0]=='0'):
            state_q0(n[1:])
        elif(n[0]=='1'):
            state_q2(n[1:])
            
def state_q2(n):
    m.append("q2")
    print("state q2")
    
    if(len(n)==0):
        print("string is not accepted")
    else:
        if(n[0]=='0'):
            state_q0(n[1:])
        elif(n[0]=='1'):
            state_q3(n[1:])
            
            
def state_q3(n):
    m.append("q3")
    print("state q3")
    
    if(len(n)==0):
        print("string accepted")
    else:
        if(n[0]=='0'):
            state_q0(n[1:])
        elif(n[0]=='1'):
            state_final(n[1:])
            
def state_final(n):
    print("\nFinal state accepted")
    print("\nString accepted")

n="0011011"
state_q0(n)

for index,i in enumerate(m):
    print(i,end="->")
else:
    print(i)