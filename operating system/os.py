from time import sleep
a=[]
for i in range(0,8):   
    n=int(input("enter a number"))
    a.append(n)
    print(a)
    sleep(1)
for i in a:
    while(i in a):
        a.pop()
        sleep(1)
        print(a)

from time import sleep
producer=[]
for i in range(0,4):
    sleep(1)
    print("is empty")
for a in range(0,4):
    n=int(input("producer produce data: "))
    print("produce data",a)
    producer.append(n)
    sleep(1)
    print(producer)
print("our data is",producer)
for i in producer:
    while(i in producer):
        producer.pop()
        sleep(1)
        print("after removing the data is:",producer)
'''

from time import sleep
producer=[]
n=int(input("enter how many sets are empty: "))
for i in range(0,n):
    sleep(1)
    print("is empty")
for a in range(0,n):
     n=int(input("enter a data: "))
     print("produce data",a)
     producer.append(n)
     sleep(1)
     print(producer)
print("our data is",producer)
for i in producer:
    while(i in producer):
        producer.pop()
        sleep(1)
        print("after removing the data is:",producer)
        
    
