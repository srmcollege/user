#singly linked list 

#traversing in singly linked list 
class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data);
            cur_node=cur_node.next;
            
    def append (self,data):
        new_node=Node(data);
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next;
        last_node.next=new_node
    
    #finding the element
    def find_index(self, key):
        current = self.head
        index = 0
        while current:
            if current.data == key:
                return index
            current = current.next
            index = index + 1
        return -1
    
    #prepending nodes in singly link list
    def prepend(self,data):
        new_node = Node (data)
        new_node.next = self.head
        self.head=new_node
        
    #deletion of node/remove node
    def RemoveNode(self, Removekey):
        HeadVal=self.head
        if (HeadVal is not None):
            if (HeadVal.data== Removekey):
                self.head=HeadVal.next
                HeadVal=None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if (HeadVal==None):
            return
        prev.next=HeadVal.next
        HeadVal = None
        
llist=LinkedList()

llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("F")
llist.prepend("A")

key=input("What Data item would you like to search ? ")

index = llist.find_index (key)
if index== -1:
    print(f"\n{key} was not found.")
else:
    print(f"\n{key} is at index {index}.")

print("  ")    

# Printing the linked list
print("Traversing in Linked List");
llist.print_list();

print("")

# Removing Node from the linked list
print("Removing Node 'A' from Linked List");
llist.RemoveNode("A")
llist.print_list();