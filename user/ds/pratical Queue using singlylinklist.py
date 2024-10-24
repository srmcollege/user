class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        removed_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_node.data

    def display(self):
        current = self.front
        if current is None:
            print("Queue is empty.")
        else:
            while current:
                if current == self.front:
                    print(f"Front -> {current.data}", end=" ")
                elif current == self.rear:
                    print(f"{current.data} <- Rear", end=" ")
                else:
                    print(current.data, end=" ")
                current = current.next
            print()

queue = Queue()

while True:
    print("\nQueue Operations:")
    print("1. Enqueue    2. Dequeue  3. Display   ")

    choice = input("enter your choice (1|2|3): ")

    if choice == '1':
        data = input("enter data to enqueue: ")
        queue.enqueue(data)
        print(f"Enqueued {data}.")
        queue.display()

    elif choice == '2':
        dequeued_item = queue.dequeue()
        if dequeued_item is not None:
            print(f"Dequeued item: {dequeued_item}")
        else:
            print("Queue is empty. Nothing to dequeue.")
        queue.display()

    elif choice == '3':
        print("Queue contents:")
        queue.display()
