
Queue=[]
size = int(input("Size of queue: "))
def Queue1():
# Enqueue
    while len(Queue) < size:
        element = input("Enter an element: ")
        Queue.append(element)
        print("The Queue is.....")
        print(Queue)
# Check if queue is full
        if len(Queue) == size:
            while True:
                choice = input("Enter 'y' to remove an element from index 0, 'n' to exit: ").lower()
                length=len(Queue)
                print("length of queue",length)
                if choice == 'y':
                    if length!=0:
                        Queue.pop(0) # Dequeue
                        print("After removing an element, Queue is...")
                        print(Queue)
                    else:
                        print("Queue is empty..")
                        break
                elif choice == 'n':
                        print("Exit.")
                        return # Exit the function
                else:
                    print("Invalid Choice...Please enter 'y' or 'n'")

Queue1()
