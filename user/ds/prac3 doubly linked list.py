class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_link_list:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
        
    #delete  program
    def delete_beginning(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None
       
        
    def delete_end(self):
        temp = self.head
        before=self.head
        while temp.next:
            temp = temp.next
            before=before.next
            before.next=None
        temp.prev = None
        
    def delete_position(self, pos):
        temp = self.head.next
        before=self.head
        for i in range(1, pos-1):
            temp = temp.next
            before=before.next
        before.next = temp.next
        temp.next.prev =before
        temp.next = None
        temp.prev = None
        
# Creating a doubly linked list
llist = Doubly_link_list()
llist.append("Atharv")
llist.append("shreyas")
llist.append("sakharam")
llist.append("prajesh")
llist.append("sanchit")
llist.append("kartik")

# Printing the linked list
print("Traversing in Doubly Linked List:")
llist.delete_position(5)
print("\nLinked List after deleting from position :")
llist.print_list()
