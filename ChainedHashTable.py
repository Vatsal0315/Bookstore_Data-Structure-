from Interfaces import Set
from DLList import DLList
import numpy as np

class ChainedHashTable(Set):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList):
        # Initialize the ChainedHashTable
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2 ** self.d)  # Initialize the table
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        # Allocate and return an array of doubly linked lists
        t = np.zeros(n, dtype=object)
        for i in range(n):
            t[i] = self.dtype()
        return t

    def _hash(self, key: object) -> int:
        # Compute the hash value for a key
        return self.z * hash(key) % (2 ** self.w) >> (self.w - self.d)

    def size(self) -> int:
        # Get the number of elements in the ChainedHashTable
        return self.n

    def find(self, key: object) -> object:
        # Find and return the value associated with a key
        lst = self.t[self._hash(key)]
        for i in range(len(lst)):
            if lst[i].key == key:
                return lst[i].value
        return None

    def add(self, key: object, value: object):
        # Add a key-value pair to the ChainedHashTable
        if self.find(key) is not None:
            return False  # Key already exists
        if self.n + 1 > len(self.t):
            self.resize()  # Resize the table if needed
        u = ChainedHashTable.Node(key, value)
        self.t[self._hash(key)].append(u)
        self.n += 1
        return True

    def remove(self, key: int) -> object:
        # Remove a key-value pair from the ChainedHashTable
        lst = self.t[self._hash(key)]
        for i in range(len(lst)):
            u = lst.get(i)
            if u.key == key:
                lst.remove(i)
                self.n -= 1
                if 3 * self.n < len(self.t):
                    self.resize()  # Resize the table if needed
                return u.value
        return None

    def resize(self):
        if self.n == len(self.t):
            self.d += 1
        else:
            self.d -= 1
        b = self.alloc_table(2 ** self.d)
        for i in range(len(self.t)):
            for j in range(self.t[i].size()):
                u = self.t[i].get(j)
                b[self._hash(u.key)].append(u)
        self.t = b

    def __str__(self):
        # Create a string representation of the ChainedHashTable
        s = "\n"
        for i in range(len(self.t)):
            s += str(i) + " : "
            for j in range(len(self.t[i])):
                k = self.t[i][j]  # jth node at ith list
                s += "(" + str(k.key) + ", " + str(k.value) + "); "
            s += "\n"
        return s
