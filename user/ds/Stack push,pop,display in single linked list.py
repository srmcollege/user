class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    
    def __init__(self):
        self.top = None

    def push(self):
        x = input("\nEnter element to be inserted into the stack: ")
        new = Node(x)
        if self.top is None:
            self.top = new
        else:
            new.next = self.top
            self.top = new
            
            
    def pop(self):
        if self.top is None:
            print("stack is empty")
        if self.top.next is None:
            print("\nPoped element is : ",self.top.data)
            self.top=None
        else:
            temp=self.top
            print("Popped element is :",self.top.data)
            self.top=temp.next
            temp=None
            
    def display (self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("\nElement in stack are :")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
            print("Top of the stack is :",self.top.data)
            
Stack = Stack()
Stack.push()
Stack.push()
Stack.push()
Stack.push()


Stack.display()

Stack.pop()
Stack.display()
