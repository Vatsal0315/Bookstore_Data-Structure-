import SLLQueue
from Interfaces import Tree


class BinaryTree(Tree):

  class Node:

    def __init__(self, key: object = None, val: object = None):
      self.parent = self.left = self.right = None
      self.k = key
      self.v = val

    def set_key(self, x):
      self.k = x

    def set_val(self, v):
      self.v = v

    def insert_left(self, u):
      self.left = u
      self.left.parent = self
      return self.left

    def insert_right(self, u):
      self.right = u
      self.right.parent = self
      return self.right

    def __str__(self):
      return f"({self.k}, {self.v})"

  def __init__(self):
    self.r = None

  def depth(self, u: Node) -> int:
    if u == self.r:
        return 0
    else:
        return 1 + self.depth(u.parent)

  def height(self) -> int:
    return self._height(self.r)

  def _height(self, u: Node) -> int:
    if u is None:
      return -1
    return 1 + max(self._height(u.left), self._height(u.right))

  def size(self) -> int:
    return self._size(self.r)

  def _size(self, u: Node) -> int:
    if u is None:
      return 0
    return 1 + self._size(u.left) + self._size(u.right)
    

  def bf_order(self):
    final = []
    if self.r is not None:
      q = SLLQueue.SLLQueue()
      q.add(self.r)
      while q.size()>0:
        u = q.remove()
        final.append(u)
        if u.left is not None:
          q.add(u.left)
        if u.right is not None:
          q.add(u.right)
    return final
  
  def in_order(self) -> list:
    return self._in_order(self.r)

  def _in_order(self, u: Node) -> list:
    final = []
    if u is None:
      return final
    final.extend(self._in_order(u.left))
    final.append(u)
    final.extend(self._in_order(u.right))
    return final

  def post_order(self) -> list:
    return self._post_order(self.r)

  def _post_order(self, u: Node):
    final = []
    if u is None:
        return final
    final.extend(self._post_order(u.left))
    final.extend(self._post_order(u.right))
    final.append(u)
    return final

  def pre_order(self) -> list:
    return self._pre_order(self.r)

  def _pre_order(self, u: Node):
    final = []
    if u is None:
      return final
    final.append(u)
    final.extend(self._pre_order(u.left))
    final.extend(self._pre_order(u.right))
    return final

  def __str__(self):
    nodes = self.bf_order()
    nodes_str = [str(node) for node in nodes]
    return ', '.join(nodes_str)