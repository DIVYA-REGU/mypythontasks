import time
import sys

class Node:
    """A class representing a node in a binary search tree."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    """A class representing the binary search tree."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Inserts a new key into the BST."""
        start_time = time.time()
        if self.root is None:
            self.root = Node(key)
            end_time = time.time()
            space_used = sys.getsizeof(self.root)  # Space for the new root node
            return (end_time - start_time), space_used  # Time and space in seconds and bytes
        else:
            return self._insert_recursive(self.root, key, start_time)

    def _insert_recursive(self, node, key, start_time):
        """Helper method to insert a new key recursively."""
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
                end_time = time.time()
                space_used = sys.getsizeof(node.left)  # Space for the new node
                return (end_time - start_time), space_used  # Time and space in seconds and bytes
            else:
                return self._insert_recursive(node.left, key, start_time)
        elif key > node.value:
            if node.right is None:
                node.right = Node(key)
                end_time = time.time()
                space_used = sys.getsizeof(node.right)  # Space for the new node
                return (end_time - start_time), space_used  # Time and space in seconds and bytes
            else:
                return self._insert_recursive(node.right, key, start_time)

    def delete(self, key):
        """Deletes a key from the BST."""
        start_time = time.time()
        self.root, time_taken, space_used = self._delete_recursive(self.root, key)
        end_time = time.time()
        return (end_time - start_time), space_used

    def _delete_recursive(self, node, key):
        """Helper method to delete a key recursively."""
        if node is None:
            return node, 0, 0  # Key not found, no time or space used
        
        time_taken, space_used = 0, 0

        if key < node.value:
            node.left, time_left, space_left = self._delete_recursive(node.left, key)
            time_taken += time_left
            space_used += space_left
        elif key > node.value:
            node.right, time_right, space_right = self._delete_recursive(node.right, key)
            time_taken += time_right
            space_used += space_right
        else:
            # Node with only one child or no child
            if node.left is None:
                space_used += sys.getsizeof(node)  # Space for current node
                return node.right, time_taken, space_used
            elif node.right is None:
                space_used += sys.getsizeof(node)  # Space for current node
                return node.left, time_taken, space_used
            
            # Node with two children: get the inorder successor
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right, time_right, space_right = self._delete_recursive(node.right, temp.value)
            time_taken += time_right
            space_used += space_right

        return node, time_taken, space_used

    def _min_value_node(self, node):
        """Finds the node with the minimum value in a given subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find(self, key):
        """Finds a key in the BST."""
        start_time = time.time()
        node, time_taken, space_used = self._find_recursive(self.root, key)
        end_time = time.time()
        return node, (end_time - start_time), space_used

    def _find_recursive(self, node, key):
        """Helper method to find a key recursively."""
        if node is None:
            return None, 0, 0  # Key not found
        
        if node.value == key:
            space_used = sys.getsizeof(node)  # Space for the found node
            return node, 0, space_used  # Key found

        if key < node.value:
            return self._find_recursive(node.left, key)
        return self._find_recursive(node.right, key)

    def inorder_traversal(self):
        """Returns the inorder traversal of the BST."""
        return self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, node):
        """Helper method for inorder traversal."""
        if node is None:
            return []
        return (self._inorder_traversal_recursive(node.left) +
                [node.value] +
                self._inorder_traversal_recursive(node.right))

    def height(self):
        """Returns the height of the tree."""
        start_time = time.time()
        height, time_taken, space_used = self._height_recursive(self.root)
        end_time = time.time()
        return height, (end_time - start_time), space_used

    def _height_recursive(self, node):
        """Helper method to find the height of the tree recursively."""
        if node is None:
            return -1, 0, 0
        
        left_height, time_left, space_left = self._height_recursive(node.left)
        right_height, time_right, space_right = self._height_recursive(node.right)

        total_time = time_left + time_right
        total_space = space_left + space_right

        return 1 + max(left_height, right_height), total_time, total_space

    def is_balanced(self):
        """Checks if the tree is balanced."""
        start_time = time.time()
        balanced, time_taken, space_used = self._is_balanced_recursive(self.root)
        end_time = time.time()
        return balanced != -1, (end_time - start_time), space_used

    def _is_balanced_recursive(self, node):
        """Helper method to check if the tree is balanced."""
        if node is None:
            return 0, 0, 0
        
        left_height, time_left, space_left = self._is_balanced_recursive(node.left)
        right_height, time_right, space_right = self._is_balanced_recursive(node.right)

        total_time = time_left + time_right
        total_space = space_left + space_right

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1, total_time, total_space
        
        return 1 + max(left_height, right_height), total_time, total_space

    def nodes_at_depth(self, depth):
        """Returns all nodes at a given depth."""
        nodes = []
        self._nodes_at_depth_recursive(self.root, depth, 0, nodes)
        return nodes

    def _nodes_at_depth_recursive(self, node, depth, current_depth, nodes):
        """Helper method to collect nodes at the given depth."""
        if node is None:
            return
        if current_depth == depth:
            nodes.append(node.value)
        else:
            self._nodes_at_depth_recursive(node.left, depth, current_depth + 1, nodes)
            self._nodes_at_depth_recursive(node.right, depth, current_depth + 1, nodes)

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Find")
        print("4. Inorder Traversal")
        print("5. Height of Tree")
        print("6. Is Balanced?")
        print("7. Nodes at Depth")
        print("8. Exit")

        choice = input("Choose an operation (1-8): ")
        
        if choice == "1":
            value = int(input("Enter value to insert: "))
            time_taken, space_used = bst.insert(value)
            print(f"Inserted {value}. Time taken: {time_taken:.10f} seconds, Space used: {space_used} bytes")
        elif choice == "2":
            value = int(input("Enter value to delete: "))
            time_taken, space_used = bst.delete(value)
            print(f"Deleted {value}. Time taken: {time_taken:.10f} seconds, Space used: {space_used} bytes")
        elif choice == "3":
            value = int(input("Enter value to find: "))
            node, time_taken, space_used = bst.find(value)
            if node:
                print(f"Node {value} found in the BST.")
            else:
                print(f"Node {value} not found in the BST.")
            print(f"Time taken: {time_taken:.10f} seconds, Space used: {space_used} bytes")
        elif choice == "4":
            print("Inorder Traversal:", bst.inorder_traversal())
        elif choice == "5":
            height, time_taken, space_used = bst.height()
            print(f"Height of the tree: {height}. Time taken: {time_taken:.10f} seconds, Space used: {space_used} bytes")
        elif choice == "6":
            balanced, time_taken, space_used = bst.is_balanced()
            print(f"Tree is balanced: {balanced}. Time taken: {time_taken:.10f} seconds, Space used: {space_used} bytes")
        elif choice == "7":
            depth = int(input("Enter depth to find nodes: "))
            nodes = bst.nodes_at_depth(depth)
            print(f"Nodes at depth {depth}: {nodes}")
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose again.")
