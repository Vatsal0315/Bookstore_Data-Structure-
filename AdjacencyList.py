from Interfaces import Graph, List
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n: int):
        self.n = n
        self.adj = [ArrayList.ArrayList() for _ in range(n)]


    def size(self):
        return self.n
    
    def add_edge(self, i: int, j: int):
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError("i or j is out of range")
        if j not in self.adj[i]:
            self.adj[i].append(j)
    def remove_edge(self, i : int, j : int):
        for k in range(self.adj[i].size()):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return True
        return False

    def has_edge(self, i: int, j: int) -> bool:
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                return True
        return False

        

    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, i) -> List:
        in_edg = ArrayList.ArrayList()
        for k in range(len(self.adj)):
            if self.has_edge(k, i):
                in_edg.append(k)
        return in_edg

    def bfs(self, r: int):
        # todo
 
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
        seen = [False] * self.n
        # Push the start vertex onto the stack
        stack.push(r)
        # While the stack is not empty, visit the next vertex in the stack
        while stack.n != 0:
            # Get the next vertex in the stack and its neighbors
            current = stack.pop()
            #neighbors = []
            # Visit the current vertex if it has not been visited yet
            if not seen[current]:
                # Append the current vertex to the traversal and mark it as seen
                traversal.append(current)
                seen[current] = True
                neighbors = self.out_edges(current)
            # Push each unvisited neighbor onto the stack
                for neighbor in reversed(neighbors):
                    if not seen[neighbor]:
                        stack.push(neighbor)
        # Return the order in which vertices were visited
        return traversal
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s
    def size(self):
        return self.n
    
