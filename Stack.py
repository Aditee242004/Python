class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} into stack")
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None
    
    def display(self):
        print("Stack contents:", self.stack)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("Popped item:", stack.pop())
    stack.display()
    print("Top item:", stack.peek())
