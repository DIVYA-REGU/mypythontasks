import time
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insertatbeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def deletefirstnode(self):
        if self.head is None:
            return
        self.head = self.head.next

    def findNode(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def delete_by_value(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next and current_node.next.data != value:
            current_node = current_node.next
        if current_node.next:
            current_node.next = current_node.next.next

    def find_index(self, value):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.data == value:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def reverselist(self):
        prev = None
        current = self.head
        while current:
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
        self.head = prev

# Helper function to measure time complexity
def measure_time(func, llist, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

# Helper function to measure space complexity
def measure_space(llist):
    # Estimating space complexity by calculating size of list and nodes
    size = sys.getsizeof(llist)
    current_node = llist.head
    while current_node:
        size += sys.getsizeof(current_node)
        current_node = current_node.next
    return size

# Main function to interact with user and test complexity
def main():
    l1 = linkedlist()

    print("Choose an operation:")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Delete first node")
    print("4. Find node")
    print("5. Delete node by value")
    print("6. Find index of value")
    print("7. Reverse list")

    choice = int(input("Enter your choice: "))1

    if choice == 1:
        data = int(input("Enter value to insert at beginning: "))
        time_taken = measure_time(l1.insertatbeginning, l1, data)
    elif choice == 2:
        data = int(input("Enter value to insert at end: "))
        time_taken = measure_time(l1.insertAtEnd, l1, data)
    elif choice == 3:
        time_taken = measure_time(l1.deletefirstnode, l1)
    elif choice == 4:
        data = int(input("Enter value to find: "))
        time_taken = measure_time(l1.findNode, l1, data)
    elif choice == 5:
        data = int(input("Enter value to delete: "))
        time_taken = measure_time(l1.delete_by_value, l1, data)
    elif choice == 6:
        data = int(input("Enter value to find index: "))
        time_taken = measure_time(l1.find_index, l1, data)
    elif choice == 7:
        time_taken = measure_time(l1.reverselist, l1)
    else:
        print("Invalid choice")
        return

    space_taken = measure_space(l1)

    print(f"Time taken: {time_taken:.6f} seconds")
    print(f"Space taken: {space_taken} bytes")

if __name__ == "__main__":
    main()
