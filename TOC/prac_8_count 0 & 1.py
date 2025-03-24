
a=0 
b=0
def state_q0(n):
    global a,b
    if len(n)==0:
        state_q2()
    else:
        if n[0]=="0":
            a+=1
            state_q1(n[1:])
        elif n[0]=="1":
            b+=1
            state_q0(n[1:])
            
def state_q1(n):
    global a,b
    if len(n)==0:
        state_q2()
    else:
        if n[0]=="0":
            a+=1
            state_q1(n[1:])
        elif n[0]=="1":
            b+=1
            state_q0(n[1:])

def state_q2():
    global a,b
    print (f"Number if 0's = {a} and Number of 1's = {b}");
n="1100101"
state_q0(n)