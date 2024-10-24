class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class double_LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        if self.head is None:
            new_node=Node(data)
            new_node.prev=None
            self.head = new_node
        else:
           new_node = Node(data)
           cur_node = self.head
           while cur_node.next:
                cur_node = cur_node.next
           cur_node.next = new_node
           cur_node.prev=None

# Test the LinkedList
llist = double_LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")

print("Traversing the linked list:")
llist.print_list()

###Insertion 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class double_LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
    def append(self, data):
        if self.head is None:
            new_node=Node(data)
            new_node.prev=None
            self.head = new_node
        else:
           new_node = Node(data)
           cur_node = self.head
           while cur_node.next:
                cur_node = cur_node.next
           cur_node.next = new_node
           cur_node.prev=None


            
llist =double_LinkedList()


llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")


llist.print_list() 


def insert_begining(self,data):
        n=Node(data)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
def insert_end(self, data):
        n=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp

def insert_position(self, pos ,data):
         n=Node(data)
         temp=self.head
         for i in range(0, pos-1):
             temp=temp.next
         n.prev=temp.next
         n.next=temp.next
         temp.next.prev=n
         temp.next=n

def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None
        
def delete_end(self):
        temp=self.head.next
        before=self.head
        while temp.next is not None:
            temp=temp.next
        before=before.next
        before.next=None
        temp.prev=None
def delete_posotion(self,pos):
        temp=self.head.next
        before=self.head
        for i in range(0,pos-1):
            temp=temp.next
            before=before.next
            before.next=temp.next
            temp.next.prev=before
            temp.next=None
            temp.previous=None

llist =double_LinkedList()


llist.delete_beginning()
llist.delete_end()
llist.delete_posotion(3)
llist.print_list()

llist =double_LinkedList()

llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")

#print("Traversing the linked list:")

llist.insert_begining("G")
llist.insert_end("cur_node")
llist.insert_position(3,"F")
llist.print_list()



