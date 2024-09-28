import time
import sys

class Node:
    """Node class for the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """Stack implementation using a linked list."""
    def __init__(self):
        self.top = None

    def push(self, data):
        """Pushes a new item onto the stack."""
        start_time = time.time()  # Start time for performance measurement
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        end_time = time.time()  # End time for performance measurement
        
        # Time and Space Complexity
        time_complexity = end_time - start_time
        space_complexity = sys.getsizeof(new_node)  # Memory used by the new node
        print(f"Push - Time Complexity: O(1), Space Complexity: {space_complexity} bytes (Execution Time: {time_complexity:.10f}s)")

    def pop(self):
        """Removes the top item from the stack and returns it."""
        start_time = time.time()  # Start time for performance measurement
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            end_time = time.time()  # End time for performance measurement
            print(f"Pop - Time Complexity: O(1), Space Complexity: O(1) (Execution Time: {end_time - start_time:.10f}s)")
            return None
        
        popped_node = self.top
        self.top = self.top.next
        end_time = time.time()  # End time for performance measurement
        
        # Time and Space Complexity
        time_complexity = end_time - start_time
        space_complexity = sys.getsizeof(popped_node)  # Memory used by the popped node
        print(f"Pop - Time Complexity: O(1), Space Complexity: {space_complexity} bytes (Execution Time: {time_complexity:.10f}s)")
        return popped_node.data

    def peek(self):
        """Returns the top item from the stack without removing it."""
        start_time = time.time()  # Start time for performance measurement
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            end_time = time.time()  # End time for performance measurement
            print(f"Peek - Time Complexity: O(1), Space Complexity: O(1) (Execution Time: {end_time - start_time:.10f}s)")
            return None
        
        end_time = time.time()  # End time for performance measurement
        
        # Time and Space Complexity
        time_complexity = end_time - start_time
        print(f"Peek - Time Complexity: O(1), Space Complexity: O(1) (Execution Time: {time_complexity:.10f}s)")
        return self.top.data

    def is_empty(self):
        """Checks if the stack is empty."""
        return self.top is None

    def display(self):
        """Displays the stack."""
        current = self.top
        if not current:
            print("The stack is empty.")
            return
        stack_elements = []
        while current:
            stack_elements.append(current.data)
            current = current.next
        print("Stack (top to bottom):", " -> ".join(map(str, stack_elements)))

# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            data = int(input("Enter data to push onto stack: "))
            stack.push(data)
        elif choice == '2':
            popped_data = stack.pop()
            if popped_data is not None:
                print(f"Popped data: {popped_data}")
        elif choice == '3':
            top_data = stack.peek()
            if top_data is not None:
                print(f"Top data: {top_data}")
        elif choice == '4':
            stack.display()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
