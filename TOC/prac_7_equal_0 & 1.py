a=0
b=0

def state_q0(n):
    global a,b
    if(len(n)== 0):
        state_q2()
    else:
        if(n[0]=="0"):
            a+=1
            state_q0(n[1:])
        elif(n[0]=="1"):
            b+=1
            state_q1(n[1:])

def state_q1(n):
    global a,b
    if(len(n)==0):
        state_q2()
    else:
        if(n[0]=="1"):
            b+=1
            state_q1(n[1:])
        elif(n[0]=="0"):
            a+=1
            state_q0(n[1:])
            
def state_q2():
    global a,b
    print("Number of '0' are ",a)
    print("Number of '1' are ",b)
    
    if(a==b):
        print("No of '0' & '1' are equal")
        print("String is accepted")
    else:
        print("No of '0' & '1' are not equal")
        print("String is not accepted")
        
n="10101110"
state_q0(n)
        