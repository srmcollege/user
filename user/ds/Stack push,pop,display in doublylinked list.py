class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Stack:
    
    def __init__(self):
        self.top = None

    def push(self):
        x = int(input("Enter element to be inserted into the stack: "))
        new_node = Node(x)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top.prev = new_node
            self.top = new_node
            
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            popped_node = self.top
            print("Popped element is :", popped_node.data)
            self.top = self.top.next
            if self.top is not None:
                self.top.prev = None
            popped_node = None
            
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Elements in stack are :")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
            print("Top of the stack is :", self.top.data)

# Example usage
stack = Stack()
stack.push()
stack.push()
stack.push()
stack.push()

stack.display()

stack.pop()
stack.display()
