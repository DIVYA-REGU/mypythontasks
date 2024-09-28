import time
import sys

class Node:
    """Node class for the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """Queue implementation using a linked list."""
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        """Adds an item to the back of the queue."""
        start_time = time.time()  # Start time for performance measurement
        new_node = Node(data)
        
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        
        if not self.front:  # If the queue was empty
            self.front = new_node
            
        end_time = time.time()  # End time for performance measurement
        
        # Time and Space Complexity
        time_complexity = end_time - start_time
        space_complexity = sys.getsizeof(new_node)  # Memory used by the new node
        print(f"Enqueue - Time Complexity: O(1), Space Complexity: {space_complexity} bytes (Execution Time: {time_complexity:.10f}s)")

    def dequeue(self):
        """Removes and returns the front item from the queue."""
        start_time = time.time()  # Start time for performance measurement
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            end_time = time.time()  # End time for performance measurement
            print(f"Dequeue - Time Complexity: O(1), Space Complexity: O(1) (Execution Time: {end_time - start_time:.10f}s)")
            return None
        
        dequeued_node = self.front
        self.front = self.front.next
        if not self.front:  # If the queue is now empty
            self.rear = None
        
        end_time = time.time()  # End time for performance measurement
        
        # Time and Space Complexity
        time_complexity = end_time - start_time
        space_complexity = sys.getsizeof(dequeued_node)  # Memory used by the dequeued node
        print(f"Dequeue - Time Complexity: O(1), Space Complexity: {space_complexity} bytes (Execution Time: {time_complexity:.10f}s)")
        return dequeued_node.data

    def peek(self):
        """Returns the front item from the queue without removing it."""
        start_time = time.time()  # Start time for performance measurement
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            end_time = time.time()  # End time for performance measurement
            print(f"Peek - Time Complexity: O(1), Space Complexity: O(1) (Execution Time: {end_time - start_time:.10f}s)")
            return None
        
        end_time = time.time()  # End time for performance measurement
        
        # Time and Space Complexity
        time_complexity = end_time - start_time
        print(f"Peek - Time Complexity: O(1), Space Complexity: O(1) (Execution Time: {time_complexity:.10f}s)")
        return self.front.data

    def is_empty(self):
        """Checks if the queue is empty."""
        return self.front is None

    def display(self):
        """Displays the queue."""
        current = self.front
        if not current:
            print("The queue is empty.")
            return
        queue_elements = []
        while current:
            queue_elements.append(current.data)
            current = current.next
        print("Queue (front to rear):", " -> ".join(map(str, queue_elements)))

    def reverse(self):
        """Reverses the linked list representing the queue."""
        start_time = time.time()  # Start time for performance measurement
        prev = None
        current = self.front
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.front, self.rear = self.rear, self.front  # Swap front and rear
        end_time = time.time()  # End time for performance measurement
        
        # Time and Space Complexity
        time_complexity = end_time - start_time
        print(f"Reverse Queue - Time Complexity: O(n), Space Complexity: O(1) (Execution Time: {time_complexity:.10f}s)")

# Example usage
if __name__ == "__main__":
    queue = Queue()
    
    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display Queue")
        print("5. Reverse Queue")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            data = int(input("Enter data to enqueue: "))
            queue.enqueue(data)
        elif choice == '2':
            dequeued_data = queue.dequeue()
            if dequeued_data is not None:
                print(f"Dequeued data: {dequeued_data}")
        elif choice == '3':
            front_data = queue.peek()
            if front_data is not None:
                print(f"Front data: {front_data}")
        elif choice == '4':
            queue.display()
        elif choice == '5':
            queue.reverse()
            print("Queue reversed.")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
