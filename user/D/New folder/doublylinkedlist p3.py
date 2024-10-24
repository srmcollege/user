class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="      ")
            current = current.next
        print()
#INSERTON
    def beg_add(self,data):
        n=Node(data)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def end_add(self,data):
        n=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def mid_add(self,data,pos):
        n=Node(data)
        temp=self.head
        for i in range(0,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
#DELETION
    def beg_del(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None
    def end_del(self):
        temp=self.head.next
        before=self.head
        while temp.next is not None:
            temp=temp.next
            before=before.next
        before.next=None
        temp.prev=None
    def mid_del(self,pos):
        temp=self.head.next
        before=self.head  
        for i in range(0,pos-1):
            temp=temp.next
            before=before.next
        before.next=temp.next
        temp.next.prev=before
        temp.next=None
        temp.prev=None
           
dllist = DoublyLinkedList()
dllist.append("A")
dllist.append("B")
dllist.append("C")
dllist.append("D")
dllist.append("E")
print("adding node at beggining")
dllist.beg_add(3)
dllist.print_list()
print()
print("adding node at end")
dllist.end_add(5)
dllist.print_list()
print()
print("adding at specific position")
dllist.mid_add(9,4)
dllist.print_list()
print()
print("Doubly linked list is   :")
dllist.print_list()
print()
print("delete from beggining")
dllist.beg_del()
dllist.print_list()
print()
print("delete from end")
dllist.end_del()
dllist.print_list()
print()
print("delete from specific position")
dllist.mid_del(4)
dllist.print_list()

