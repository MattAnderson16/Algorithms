class stack:
    """Stack class"""
    def __init__(self):
        self.items = []
        self.max_size = None
        self.stack_pointer = None
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    def push(self,item_to_add):
        if len(self.items) < self.max_size:
            self.items.append(item_to_add)
            if len(self.items) == 1:
                self.stack_pointer = 0
            else:
                self.stack_pointer += 1
    def pop(self):
        if len(self.items) > 0:
            item = self.items[self.stack_pointer]
            self.items.pop(self.stack_pointer)
            if self.stack_pointer > 0:
                self.stack_pointer -= 1
            else:
                self.stack_pointer = None
            return item
    def peek(self):
        return self.items[self.stack_pointer - 1]
    def size(self,max_size):
        self.max_size = max_size

if __name__ == "__main__":   
    stack = stack()
    print(stack.items)
    print(stack.is_empty())
    stack.size(6)
    stack.push("a")
    print(stack.items)
    print(stack.is_empty())
    stack.peek()
    stack.push("b")
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
