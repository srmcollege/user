
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
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
      
        return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def find_index(self, key):
        current = self.head
        index = 0
        while current:
            if current.data == key:
                return index
            current = current.next
            index += 1
        return -1 

#Example usage
llist = LinkedList()
for data in [4, -3, 1, 0, 9, 11]:
    llist.append(data)
    
print("The linked list: ", end=' ')
llist.print_list()
print()


key = int(input("What data item would you like to search? "))
index = llist.find_index(key)
if index == -1:
    print(str(key) + 'was not found.')
else:
    print(str(key) + ' is at index ' + str(index) + '.')


def prepend (self,data):
    new_node=node(data)
    new_node.next=self.head
    self.head=new_node
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend:("E")
llist.prepend:("F")
print("traversing in linklist")
llist.print_list()
