import numpy as np
from Interfaces import Queue

class ArrayQueue(Queue):
    def __init__(self):
        # Initialize the state (queue size, front index, and internal array)
        self.n = 0  # Number of elements in the queue
        self.j = 0  # Index of the front element
        self.a = self.new_array(1)  # Internal array to store elements

    def new_array(self, n: int) -> np.array:
        # Create a new array of size 'n'
        return np.zeros(n, object)

    def resize(self):
        '''
        resize: Resize the internal array when it becomes full or too empty.
        '''
        b = self.new_array(max(1, 2 * self.n))
        for i in range(self.n):
            # Copy elements from the old array to the new array, considering circular indexing.
            b[i] = self.a[(self.j + i) % len(self.a)]
        self.a = b
        self.j = 0

    def add(self, x: object):
        '''
        add: Add an element 'x' to the end of the queue, potentially resizing the array.
        Input:
            x: Object type, i.e., any object to be added to the queue.
        '''
        if self.n == len(self.a):
            # If the internal array is full, resize it to accommodate more elements.
            self.resize()
        
        # Calculate the index where 'x' will be added, considering wrapping around the circular array.
        # Append 'x' to the end of the array and increment the size.
        self.a[(self.j + self.n) % len(self.a)] = x
        self.n += 1

    def remove(self) -> object:
        '''
        remove: Remove and return the front element of the queue.
        Returns:
            The removed element.
        Raises:
            IndexError if the queue is empty.
        '''
        if self.n == 0:
            raise IndexError('Queue is empty')
        
        # Get the front element of the queue and update the front index and size.
        x = self.a[self.j]
        self.j = (self.j + 1) % len(self.a)
        self.n -= 1

        # Check if the array has become too empty and needs resizing.
        if self.n < len(self.a) // 4:
            self.resize()
        
        return x

    def size(self):
        '''
        size: Return the number of elements in the queue.
        '''
        return self.n

    def __str__(self):
        '''
        __str__: Return a string representation of the queue.
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        '''
        __iter__: Initialize the iterator for iterating over the queue.
        '''
        self.iterator = 0
        return self

    def __next__(self):
        '''
        __next__: Get the next element in the iteration.
        '''
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
