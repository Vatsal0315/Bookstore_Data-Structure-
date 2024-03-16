from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np

class AdjacencyMatrix(Graph):
    def __init__(self, n: int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)
        self.a = [[False] * n for _ in range(self.n)]

    def size(self):
        return self.n

    def add_edge(self, i: int, j: int):
        if 0 <= i < self.n and 0 <= j < self.n:
            self.adj[i][j] = 1

    def remove_edge(self, i: int, j: int):
        if self.adj[i][j] == 0:
            return False
        self.adj[i][j] = 0
        return True

    def has_edge(self, i: int, j: int) -> bool:
        return self.adj[i][j]

    def out_edges(self, i) -> List:
        edge = []
        for j in range(self.n):
            if self.adj[i][j] == 1:
                edge.append(j)
        return edge
 

    def in_edges(self, i) -> List:
        edge = []
        for j in range(self.n):
            if self.adj[j][i] == 1:
                edge.append(j)
        return edge
    
    def bfs(self, r: int):
        # Initialize empty list traversal to store the order that vertices are visited
        traversal = []
        # Initialize array seen of n Boolean values to False
        seen = [False] * self.n
        # Initialize empty queue q to keep track of vertices to visit
        queue = ArrayQueue.ArrayQueue()
        # Visit the start vertex and add it to the queue and traversal
        queue.add(r)
        traversal.append(r)
        seen[r] = True
        # While the queue is not empty, visit the next vertex in the queue
        while queue.n != 0:
            current = queue.remove()
            neighbors = self.out_edges(current)
            # Visit each neighbor of the current vertex
            for neighbor in neighbors:
                # Add the neighbor to the queue, traversal, and mark it as seen
                if not seen[neighbor]:
                    queue.add(neighbor)
                    traversal.append(neighbor)
                    seen[neighbor] = True
        # Return the order in which vertices were visited
        return traversal

    def dfs(self, r: int):
        # Initialize empty list traversal to store the order that vertices are visited
        traversal = []
        # Initialize empty stack s to keep track of vertices to visit
        stack = ArrayStack.ArrayStack()
        # Initialize array seen of n Boolean values to False
        seen = []
        for j in range(self.n):
            seen.append(False)
        # Push the start vertex onto the stack
        stack.push(r)
        # While the stack is not empty, visit the next vertex in the stack
        while stack.n != 0:
            # Get the next vertex in the stack and its neighbors
            current = stack.pop()
            neighbors = []
            # Visit the current vertex if it has not been visited yet
            if not seen[current]:
                # Append the current vertex to the traversal and mark it as seen
                traversal.append(current)
                seen[current] = True
            for j in range(self.n):
                if self.has_edge(current, j) == True:
                    neighbors.append(j)
            # Push each unvisited neighbor onto the stack
            for neighbor in neighbors[::-1]:
                if not seen[neighbor]:
                    stack.push(neighbor)
        # Return the order in which vertices were visited
        return traversal

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s

