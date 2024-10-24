
#Stack operation
class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
class stack:
    def __init__(self):
        self.top = None
    def push(self):
        x=int(input("Enter element to the stack"))
        new=Node(x)
        if self.top is None:
            self.top=new
            self.top.next=None
        else:
            new.next=self.top
            self.top=new

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        if self.top.next is None:
            print("Popped elements is:",self.top.data)
            print(".....................")
            self.top=None
        else:
            temp=self.top
            print("Poped element is", self.top.data)
            print(".......................................")
            self.top=temp.next
            temp=None
    def display(self):
        if self.top is None:
            print("Stack is empty")
            print("...............")
        else:
            print("Element in stack")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
            print("Top of stack",self.top.data)


stack=stack()
stack.push()
stack.push()
stack.push()
stack.push()
stack.push()
stack.display()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.display()
