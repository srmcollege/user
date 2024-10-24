class Node:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert_element(self, item, priority):
        new_node = Node(item, priority)
      
        if len(self.queue) == 0:
            self.queue.append(new_node)
        else:
           
            for i in range(len(self.queue)):
                if new_node.priority < self.queue[i].priority:
                    self.queue.insert(i, new_node)
                    return
           
            self.queue.append(new_node)

    def display(self):
        if not self.queue:
            print("The priority queue is empty.")
        else:
            print("Priority queue is:")
            for node in self.queue:
                print(f"Item: {node.item}, Priority: {node.priority}")

    def size(self):
        return len(self.queue)

    def remove_highest_priority(self):
        if self.size() == 0:
            print("The queue is empty.")
            return None
        return self.queue.pop(0) 

# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert_element('C', 3)
    pq.insert_element('A', 1)
    pq.insert_element('B', 2)

    pq.display()  

    removed_item = pq.remove_highest_priority()  
    if removed_item:
        print(f"Removed item: {removed_item.item}, Priority: {removed_item.priority}")

    pq.display()  

