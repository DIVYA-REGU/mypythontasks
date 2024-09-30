import time
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Inserts a new node at the beginning of the linked list."""
        start_time = time.time()  # Start time for performance measurement
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        end_time = time.time()  # End time for performance measurement

        # Time and Space Complexity
        time_complexity = end_time - start_time
        space_complexity = sys.getsizeof(new_node)  # Memory used by the new node
        print(f"Insert at Beginning - Time Complexity: O(1), Space Complexity: {space_complexity} bytes (Execution Time: {time_complexity:.10f}s)")

    def insert_at_end(self, data):
        """Inserts a new node at the end of the linked list."""
        start_time = time.time()  # Start time for performance measurement
        new_node = Node(data)
        
        if not self.head:  # If the list is empty
            self.head = new_node
            end_time = time.time()  # End time for performance measurement
            print(f"Insert at End (empty list) - Time Complexity: O(1), Space Complexity: {sys.getsizeof(new_node)} bytes (Execution Time: {end_time - start_time:.10f}s)")
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        end_time = time.time()  # End time for performance measurement

        # Time and Space Complexity
        time_complexity = end_time - start_time
        space_complexity = sys.getsizeof(new_node)  # Memory used by the new node
        print(f"Insert at End - Time Complexity: O(n), Space Complexity: {space_complexity} bytes (Execution Time: {time_complexity:.10f}s)")

    def delete_node(self, key):
        """Deletes a node with the specified key."""
        start_time = time.time()  # Start time for performance measurement
        current = self.head

        # If the list is empty
        if not current:
            print("List is empty. Cannot delete.")
            end_time = time.time()  # End time for performance measurement
            print(f"Delete Node - Time Complexity: O(n), Space Complexity: O(1) (Execution Time: {end_time - start_time:.10f}s)")
            return

        # If the node to be deleted is the head node
        if current.data == key:
            self.head = current.next
            current = None
            end_time = time.time()  # End time for performance measurement
            print(f"Delete Node (head) - Time Complexity: O(1), Space Complexity: O(1) (Execution Time: {end_time - start_time:.10f}s)")
            return

        # Search for the node to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found
        if not current:
            print("Node not found.")
            end_time = time.time()  # End time for performance measurement
            print(f"Delete Node - Time Complexity: O(n), Space Complexity: O(1) (Execution Time: {end_time - start_time:.10f}s)")
            return

        # Unlink the node
        prev.next = current.next
        current = None
        end_time = time.time()  # End time for performance measurement
        print(f"Delete Node - Time Complexity: O(n), Space Complexity: O(1) (Execution Time: {end_time - start_time:.10f}s)")

    def find_node(self, key):
        """Finds a node with the specified key."""
        start_time = time.time()  # Start time for performance measurement
        current = self.head
        while current:
            if current.data == key:
                end_time = time.time()  # End time for performance measurement
                print(f"Find Node - Time Complexity: O(n), Space Complexity: O(1) (Execution Time: {end_time - start_time:.10f}s)")
                return current
            current = current.next
        end_time = time.time()  # End time for performance measurement
        print(f"Find Node - Time Complexity: O(n), Space Complexity: O(1) (Execution Time: {end_time - start_time:.10f}s)")
        return None

    def display(self):
        """Displays the linked list."""
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()
    
    while True:
        print("\nMenu:")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete Node")
        print("4. Find Node")
        print("5. Display List")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            data = int(input("Enter data to insert at beginning: "))
            linked_list.insert_at_beginning(data)
        elif choice == '2':
            data = int(input("Enter data to insert at end: "))
            linked_list.insert_at_end(data)
        elif choice == '3':
            key = int(input("Enter key to delete: "))
            linked_list.delete_node(key)
        elif choice == '4':
            key = int(input("Enter key to find: "))
            found_node = linked_list.find_node(key)
            if found_node:
                print(f"Node with data {found_node.data} found.")
            else:
                print("Node not found.")
        elif choice == '5':
            linked_list.display()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
