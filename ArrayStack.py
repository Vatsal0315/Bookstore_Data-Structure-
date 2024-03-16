import numpy as np
from Interfaces import Stack
from Interfaces import List

class ArrayStack(Stack, List):
    '''
    ArrayStack: Implementation of the Stack interface based on Arrays.
    This class inherits from both the Stack and List interfaces.
    All the @abstractmethod should be implemented.
    An instance of ArrayStack has access to all the methods in ArrayStack and
    all the methods of the base class (Stack). When executing a method, it executes
    the method of ArrayStack if it exists; otherwise, it executes the method in the
    base class (Stack).
    
    For example,
    s = ArrayStack()
    print(s)
    print(len(s))
    '''
    def __init__(self):
        # Initialize the state (array and size)
        self.a = self.new_array(1)  # Internal array to store elements
        self.n = 0  # Number of elements in the stack

    def new_array(self, n: int) -> np.array:
        # Create a new array of size 'n'
        return np.zeros(n, object)

    def resize(self):
        '''
        resize: Resize the internal array when it becomes full or too empty.
        '''
        b = self.new_array(max(1, 2 * self.n))
        for i in range(self.n):
            # Copy elements from the old array to the new array.
            b[i] = self.a[i]
        self.a = b

    def add(self, i: int, x: object):
        '''
        add: Shift all elements with indices greater than 'i' one position to the right
        and add element 'x' at position 'i'.
        Input:
            i: Index where 'x' will be inserted.
            x: Object type, i.e., any object to be added to the stack.
        '''
        if self.n == len(self.a):
            # If the internal array is full, resize it to accommodate more elements.
            self.resize()
        for j in range(self.n, i, -1):
            self.a[j] = self.a[j - 1]
        self.a[i] = x
        self.n += 1

    def remove(self, i: int) -> object:
        '''
        remove: Remove the element at index 'i' and shift all elements with indices greater than 'i' one
        position to the left.
        Input:
            i: Index of the element to be removed.
        Returns:
            The removed element.
        '''
        if self.n == 0:
            raise IndexError()
        x = self.a[i]
        for j in range(i, self.n - 1):
            self.a[j] = self.a[j + 1]
        self.n -= 1
        if len(self.a) >= 3 * self.n:
            self.resize()
        return x

    def push(self, x: object):
        '''
        push: Add an element 'x' to the top of the stack.
        Input:
            x: Object type, i.e., any object to be added to the stack.
        '''
        self.add(self.n, x)

    def pop(self) -> object:
        '''
        pop: Remove and return the element from the top of the stack.
        Returns:
            The removed element.
        '''
        return self.remove(self.n - 1)

    def size(self):
        '''
        size: Returns the size of the stack.
        Return: An integer greater than or equal to zero representing the number
                of elements in the stack.
        '''
        return self.n

    def __str__(self) -> str:
        '''
        __str__: Returns a string representation of the stack.
        Return: A string with the content of the stack.
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        '''
        Initialize the iterator. It is to be used in a for loop.
        '''
        self.iterator = 0
        return self

    def __next__(self):
        '''
        Move to the next item. It is to be used in a for loop.
        '''
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
