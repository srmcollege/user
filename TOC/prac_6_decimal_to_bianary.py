1# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:51:13 2025

@author: ASUS
"""


#Program for decimal no. divisible by 2 
decimal_num=int(input("Enter the Number : ")) 
binary_num=bin(decimal_num)[2:]
#print binary_num
bnum=str(binary_num) 
a=(bnum[-1])

def state_q0():
    print("state q0")
    print("The decimal number: ",decimal_num)
    print("By converting to the binary num:", binary_num) 
    print("Number is divisible by 2")
    
def state_q1():
    print("state q1")
    print("The decimal number: ",decimal_num)
    print("By converting to the binary num:", binary_num)
    print("Number is NOT divisible by 2")
    
if a=="0":
    state_q0() 
else:
    state_q1()