import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree
 
 
def left(i: int) -> int:
    if i< 0: raise IndexError()
    return 2*i + 1
 
 
def right(i: int) -> int:
    if i< 0: raise IndexError()
    return 2*(i+1)
 
 
def parent(i: int) -> int:
    if i< 0: raise IndexError()
    return (i-1)//2
 
 
def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)
 
 
class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0
 
    def add(self, x: object):
        if len(self.a) == self.n:
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True
 
    def remove(self):
        if self.n == 0:
            raise IndexError
        x = self.a[0]
        self.a[0] = self.a[self.n -1]
        self.n -= 1
        self._trickle_down_root()
        if 3*self.n < len(self.a):
            self._resize()
        return x
 
 
    def depth(self, u) -> int:
        return self._depth(u, 0, 0)
 
    def height(self) -> int:
        return int(math.log2(self.n - 1))  # O(1) time complexity
 
    def bf_order(self) -> list:
        if self.n == 0:
            return []
        q = []
        res = []
        q.append(0)
        while len(q) > 0:
            curr = q.pop(0)
            res.append(self.a[curr])
            left_child = left(curr)
            right_child = right(curr)
            if left_child < self.n:
                q.append(left_child)
            if right_child < self.n:
                q.append(right_child)
        return res
 
    def in_order(self) -> list:
        return self._in_order(0)
 
    def post_order(self) -> list:
        result = []
        self._post_order_helper(0, result)
        return result
    def _post_order_helper(self, i: int, result: list) -> None:
 
        left_child = left(i)
        right_child = right(i)
        if left_child < self.n:
            self._post_order_helper(left_child, result)
        if right_child < self.n:
            self._post_order_helper(right_child, result)
        result.append(self.a[i])
 
    def pre_order(self) -> list:
        return self._pre_order(0)
    
    def _pre_order(self, i):
        nodes = []
        nodes.append(self.a[i])
        if left(i) < self.n:
            nodes.extend(self._pre_order(left(i)))
        if right(i) < self.n:
            nodes.extend(self._pre_order(right(i)))
        return nodes
 
    def _depth(self, u, i, d) -> int:
        if i >= self.n:
            raise ValueError(f"{u} is not found in the binary tree.")
        if self.a[i] == u:
            return d
        left_child = left(i)
        right_child = right(i)
        if left_child < self.n:
            left_depth = self._depth(u, left_child, d + 1)
            if left_depth is not None:
                return left_depth
        if right_child < self.n:
            right_depth = self._depth(u, right_child, d + 1)
            if right_depth is not None:
                return right_depth
        return None
 
    def _in_order(self, i) -> list:
        res = []
        if i < self.n:
            res.extend(self._in_order(left(i)))
            res.append(self.a[i])
            res.extend(self._in_order(right(i)))
        return res
 
    def _post_order(self, i) -> list:
        res = []
        if i < self.n:
            res.extend
 
    def size(self) -> int:
        return self.n
 
    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]
 
    def _bubble_up_last(self):
        i = self.n - 1
        p_idx = parent(i)
        while i > 0 and self.a[i] < self.a[p_idx]:
            self.a[i],self.a[p_idx] = self.a[p_idx], self.a[i]
            i = p_idx
            p_idx = parent(i)
    
 
    def _resize(self):
        self.j = 0
        b = _new_array(max(1, 2 * self.n))
        for i in range(self.n):
            b[i] = self.a[(self.j+i)%len(self.a)]
        self.a = b
 
    def _trickle_down_root(self):
        i = 0
        l_idx = left(i)
        r_idx = right(i)
        valid = i < self.n and (l_idx < self.n or r_idx < self.n)
 
        while valid and (self.a[i] > self.a[l_idx] or self.a[i] > self.a[r_idx]):
 
            if self.a[l_idx] < self.a[i]:
                min_idx = l_idx
            else:
                min_idx = i
 
            if self.a[r_idx] < self.a[min_idx]:
                min_idx = r_idx
 
            temp = self.a[min_idx]
            self.a[min_idx] = self.a[i]
            self.a[i] = temp
 
            i = min_idx
            l_idx = left(i)
            r_idx = right(i)
            valid = i < self.n and (l_idx < self.n or r_idx < self.n)
 
        return
 
 
 
    def __str__(self):
        return str(self.a[0:self.n])