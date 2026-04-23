# Queue implementation using deque with safe_dequeue()

from collections import deque

class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.queue = deque()

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.queue.append(item)
        print(f"Enqueued {item}.")

    def safe_dequeue(self):
        """Safely remove the front item from the queue."""
        if not self.queue:
            print("Queue is empty, cannot dequeue.")
            return None
        return self.queue.popleft()

    def display(self):
        """Display the current queue."""
        print("Current queue:", list(self.queue))

# Example usage
if __name__ == "__main__":
    my_queue = Queue()
    my_queue.safe_dequeue()
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.display()
    print("Dequeued item:", my_queue.safe_dequeue())
    my_queue.display()
