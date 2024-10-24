import sys

try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

size=int(input("Enter the size of the table"))
ht=[None]*size

def hashcode(x):
    return x%size

def insert(x):
    hc=hashcode(x)
    if ht[hc]==None:
        ht[hc]=x
        print(x,"is inserted at",hc)
        return
    t=(hc+1)
    
    while t!=hc and ht[t]!=None:
        t=(t+1)
        print("t =",+t)
    if ht[t]==None:
        ht[t]=x
        print(x,"is inserted at",t)
        return
    color.write("The value could not be inserted \n","COMMENT")
    
def search(x):
    hc=hashcode(x)
    if ht[hc]==x:
        print(x,"is found at",hc)
        return hc
    t=(hc+1)%size
    while t !=hc and ht[t]!= x:
        t=(t+1)%size
    if ht[t]==x:
        print(x,"is not found in the hash table")
        return -1

def delete(x):
    a=search(x)
    print(x,"is deleted")
    if x==1:
        print(x,"is not found in hashtable")
        return
    ht[a]=None

def display():
    for i in range(size):
        print(i,end="\t")
    print()
    for i in ht:
        print(i,end="\t")
    print()

while True:
    print("1.Enter\n2.Delete\n3.Display\n4.stop")
    ch=int(input("enter choice"))
    if ch==1:
        insert(int(input("enter value to be inserted:  ")))
    elif ch==2:
        delete(int(input("enter value to be deleted:   ")))
    elif ch==3:
        display()
    else:
        break
    
