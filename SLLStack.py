from Interfaces import Stack  # Import the Stack interface

class SLLStack(Stack):
    class Node:
        def __init__(self, x: object):
            self.next = None  # Initialize the 'next' pointer of the node
            self.x = x  # Store the data in the node

    def __init__(self):
        self.head = None  # Initialize the head of the stack
        self.tail = None  # Initialize the tail (not typically used in a stack)
        self.n = 0        # Initialize the size of the stack (number of elements)

    def push(self, x: object):
        """
        Pushes an element onto the stack.
        INPUT: x - the element to push
        """
        new_node = self.Node(x)  # Create a new node with the given element
        if self.head is None:
            self.head = new_node  # If the stack is empty, set the head to the new node
        else:
            new_node.next = self.head  # Set the 'next' of the new node to the current head
            self.head = new_node  # Update the head to be the new node
        self.n += 1  # Increment the size of the stack

    def pop(self) -> object:
        """
        Pops and returns the element from the top of the stack.
        """
        if self.head is None:
            raise IndexError("Remove from empty stack")  # Raise an error if the stack is empty
        x = self.head.x  # Get the element at the top of the stack
        self.head = self.head.next  # Move the head to the next node
        self.n -= 1  # Decrement the size of the stack
        return x

    def size(self) -> int:
        """
        Returns the current size of the stack.
        """
        return self.n

    def __str__(self):
        """
        Returns a string representation of the stack.
        """
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x  # Add the element to the string
            u = u.next  # Move to the next node
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        """
        Initialize an iterator for the stack.
        """
        self.iterator = self.head
        return self

    def __next__(self):
        """
        Get the next element in the stack using the iterator.
        """
        if self.iterator is not None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()  # Raise an error when there are no more elements to iterate
        return x
