class BSTNode:
    """Node class for BST."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    """Binary Search Tree with insert, search, delete operations."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert key into BST."""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        else:
            # Key already exists, no duplicates allowed
            print(f"Warning: Key {key} already exists. Skipping insertion.")
        return node

    def search(self, key):
        """Search for key in BST. Returns True if found, else False."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def delete(self, key):
        """Delete key from BST."""
        self.root, deleted = self._delete_recursive(self.root, key)
        if not deleted:
            print(f"Warning: Key {key} not found. Cannot delete.")
        return deleted

    def _delete_recursive(self, node, key):
        if node is None:
            return node, False

        if key < node.key:
            node.left, deleted = self._delete_recursive(node.left, key)
            return node, deleted
        elif key > node.key:
            node.right, deleted = self._delete_recursive(node.right, key)
            return node, deleted

        # Node with key found
        if node.left is None and node.right is None:
            # Leaf node
            return None, True
        elif node.left is None:
            # One child (right)
            return node.right, True
        elif node.right is None:
            # One child (left)
            return node.left, True
        else:
            # Two children: find inorder successor (smallest in right subtree)
            successor = self._find_min(node.right)
            node.key = successor.key
            node.right, _ = self._delete_recursive(node.right, successor.key)
            return node, True

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder_traversal(self):
        """Return a list of keys in inorder."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

# Demonstration and test cases
if __name__ == "__main__":
    bst = BST()
    print("Inserting keys: 10, 5, 15, 3, 7, 12, 18")
    for key in [10, 5, 15, 3, 7, 12, 18]:
        bst.insert(key)

    print("Inorder traversal after insertions:", bst.inorder_traversal())

    print("\nSearching for keys 7 and 20:")
    print(f"7 found? {bst.search(7)}")
    print(f"20 found? {bst.search(20)}")

    print("\nDeleting leaf node 3:")
    bst.delete(3)
    print("Inorder traversal:", bst.inorder_traversal())

    print("\nDeleting node with one child 15:")
    bst.delete(15)
    print("Inorder traversal:", bst.inorder_traversal())

    print("\nDeleting node with two children 5:")
    bst.delete(5)
    print("Inorder traversal:", bst.inorder_traversal())

    print("\nAttempting to delete non-existent key 100:")
    bst.delete(100)
