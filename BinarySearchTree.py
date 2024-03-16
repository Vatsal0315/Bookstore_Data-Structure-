from BinaryTree import BinaryTree
from Interfaces import Set

class BinarySearchTree(BinaryTree, Set):
    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0  # Initialize the number of nodes in the tree

    def add(self, key: object, value: object = None) -> bool:
        # Create a new node with the provided key and value
        new_node = self.Node(key, value)
        # Find the parent node to add the new node as a child
        parent = self._find_last(key)
        return self._add_child(parent, new_node)

    def find(self, key: object) -> object:
        # Find a node with the given key and return its value
        node = self._find_eq(key)
        if node == None:
            return None
        return node.v

    def remove(self, key: object):
        # Find and remove a node with the given key
        u = self._find_eq(key)
        if u == None:
            raise ValueError  # If the node is not found, raise an error
        value = u.v  # Store the value of the node to be removed
        self._remove_node(u)  # Remove the node
        return value  # Return the removed value

    def _find_eq(self, key: object) -> BinaryTree.Node:
        # Find a node with the exact given key
        current = self.r
        while current is not None:
            if key < current.k:
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        return None

    def _find_last(self, key: object) -> BinaryTree.Node:
        # Find the last node with a key less than or equal to the given key
        current = self.r
        parent = None
        while current != None:
            parent = current
            if key < current.k:
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        return parent

    def _add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        # Add a child node 'u' under the parent node 'p'
        if p is None:
            self.r = u  # If parent is None, 'u' becomes the root of the tree
        else:
            if u.k < p.k:
                p.left = u
            elif u.k > p.k:
                p.right = u
            else:
                return False  # If the key already exists, return False
            u.parent = p  # Set the parent of the new node
        self.n += 1  # Increment the node count
        return True

    def _splice(self, u: BinaryTree.Node):
        # Replace 'u' with its child
        if u.left is not None:
            child = u.left
        else:
            child = u.right
        if u == self.r:
            self.r = child
            p = None
        else:
            p = u.parent
            if p.left == u:
                p.left = child
            else:
                p.right = child
        if child is not None:
            child.parent = p
        self.n += 1  # Increment the node count

    def _remove_node(self, u: BinaryTree.Node):
        # Remove the node 'u' from the tree
        if u.left == None or u.right == None:
            self._splice(u)
        else:
            w = u.right
            while w.left is not None:
                w = w.left
            u.k = w.k
            u.v = w.v
            self._splice(w)

    def clear(self):
        # Empty the BinarySearchTree by resetting the root and node count
        self.r = None
        self.n = 0

    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.k  # Yield the keys of the tree nodes
            u = self.next_node(u)

    def first_node(self):
        # Find and return the leftmost node in the tree (smallest key)
        w = self.r
        if w is None:
            return None
        while w.left is not None:
            w = w.left
        return w

    def next_node(self, w):
        if w.right is not None:
            # Find the node with the next larger key
            w = w.right
            while w.left is not None:
                w = w.left
        else:
            while w.parent is not None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w

    def find_node(self, key: object) -> BinaryTree.Node:
        # Find and return the node with the specified key
        current = self.r
        smallest = None
        while current is not None:
            if key < current.k:
                smallest = current
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        if smallest is not None:
            return smallest
        else:
            return None
