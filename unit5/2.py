# Stack implementation using list with safe_pop()

class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    def safe_pop(self):
        """Safely pop an item from the stack."""
        if not self.stack:
            print("Stack is empty, nothing to pop.")
            return None
        return self.stack.pop()

    def display(self):
        """Display the current stack."""
        print("Current stack:", self.stack)

# Example usage
if __name__ == "__main__":
    my_stack = Stack()
    my_stack.safe_pop()
    my_stack.push(10)
    my_stack.push(20)
    my_stack.display()
    print("Popped item:", my_stack.safe_pop())
    my_stack.display()
