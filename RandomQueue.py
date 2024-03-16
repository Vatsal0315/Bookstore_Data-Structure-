import random
from ArrayQueue import ArrayQueue

class RandomQueue(ArrayQueue):
    def __init__(self):
        # Initialize the RandomQueue by calling the constructor of the parent class ArrayQueue
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        # Remove a random element from the queue
        
        # Check if the queue is empty
        if self.n == 0:
            raise IndexError("Queue is empty")
        
        # Generate a random index within the range of valid elements
        rand_index = random.randint(0, self.n - 1)
        
        # Get the item at the randomly chosen index
        removed_item = self.a[(rand_index + self.j) % len(self.a)]
        
        # Mark the position as None to indicate the removal
        self.a[(rand_index + self.j) % len(self.a)] = None
        
        # Shift elements to fill the gap created by the removal
        for i in range(rand_index, self.n - 1):
            self.a[(i + self.j) % len(self.a)] = self.a[(i + self.j + 1) % len(self.a)]
        
        # Mark the last position as None
        self.a[(self.j + self.n - 1) % len(self.a)] = None
        
        # Decrement the number of elements in the queue
        self.n -= 1
        
        # Check if the array is significantly larger than the number of elements
        if len(self.a) >= 3 * self.n:
            self.resize()
        
        # Return the removed item
        return removed_item
