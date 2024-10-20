import threading
import time 
resources=0
readers=0
mutex=threading.Semaphore(1)
read_lock=threading.Semaphore(1)
writter_lock=threading.Semaphore(1)
def reader():
    global resources,readers
    read_lock.acquire()
    readers +=1
    if readers==1:
        writter_lock.acquire()
    read_lock.release()
    print("i am in readers function \n")
    time.sleep(1)
    read_lock.acquire()
    readers-=1
    if readers==0:
        writter_lock.release()
    read_lock.release()
    #resources -=1
def writter():
    global resources
    writter_lock.acquire()
    resources+=1
    print("i am inside writters function",resources)
    time.sleep(1)
    writter_lock.release()

def main():
    thread=[]
    for i in range(5):
        t=threading.Thread(target=reader)
        thread.append(t)
        t.start()
        t=threading.Thread(target=writter)
        thread.append(t)
        t.start()
    for t in thread:
        t.join()
main()
