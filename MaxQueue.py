from SLLQueue import SLLQueue
from DLLDeque import DLLDeque

class MaxQueue(SLLQueue):
    def __init__(self):
        super().__init__()
        self.max_deque = DLLDeque()

    def add(self, x: object):
        super().add(x)
        change = False
        if self.max_deque.n == 0 or x > self.max_deque.get(0):
            # Reset the max_deque with a single element
            del self.max_deque
            self.max_deque = DLLDeque()
            self.max_deque.add(0, x)
            change = True
        else:
            for i in range(1, self.max_deque.n):
                if x > self.max_deque.get(i):
                    # Update the max_deque and remove elements after the new max
                    self.max_deque.set(i, x)
                    for k in range(i + 1, self.max_deque.n):
                        self.max_deque.remove_last()
                    change = True
                    break
        if not change:
            self.max_deque.add_last(x)

    def remove(self) -> object:
        tvar = super().remove()
        
        for i in range(0, self.max_deque.n):
            if tvar == self.max_deque.get(i):
                self.max_deque.remove(i)
                break
        return tvar

    def max(self):
        # Return the first element in the doubly-linked list (i.e., the current max)
        return self.max_deque.get(0)
