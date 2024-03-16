from Interfaces import Queue  # Import the Queue interface

class SLLQueue(Queue):
    class Node:
        def __init__(self, x: object):
            self.next = None  # Initialize the 'next' pointer of the node
            self.x = x  # Store the data in the node

    def __init__(self):
        self.head = None  # Initialize the head (front) of the queue
        self.tail = None  # Initialize the tail (rear) of the queue
        self.n = 0        # Initialize the size of the queue (number of elements)

    def add(self, x: object):
        """
        Adds an element to the end of the queue.
        INPUT: x - the element to add
        """
        new_node = self.Node(x)  # Create a new node with the given element
        if self.tail is None:
            self.head = new_node  # If the queue is empty, set the head to the new node
        else:
            self.tail.next = new_node  # Set the 'next' of the current tail to the new node
        self.tail = new_node  # Update the tail to be the new node
        self.n += 1  # Increment the size of the queue

    def remove(self) -> object:
        """
        Removes and returns the element at the front of the queue.
        """
        if self.head is None:
            raise IndexError("Queue is empty")  # Raise an error if the queue is empty
        x = self.head.x  # Get the element at the front of the queue
        self.head = self.head.next  # Move the head to the next node
        if self.head is None:
            self.tail = None  # If the queue is now empty, update the tail
        self.n -= 1  # Decrement the size of the queue
        return x

    def size(self) -> int:
        """
        Returns the current size of the queue.
        """
        return self.n

    def __str__(self):
        """
        Returns a string representation of the queue.
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
        Initialize an iterator for the queue.
        """
        self.iterator = self.head
        return self

    def __next__(self):
        """
        Get the next element in the queue using the iterator.
        """
        if self.iterator is not None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()  # Raise an error when there are no more elements to iterate
        return x
