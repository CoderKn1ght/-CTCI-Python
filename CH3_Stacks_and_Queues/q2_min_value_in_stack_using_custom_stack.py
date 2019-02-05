class Stack(object):
    def __init__(self):
        self.stack = []
        self.min_values = []

    def get_size(self):
        return len(self.stack)

    def push(self, val):
        if self.get_size() == 0:
            self.min_values.append(val)
        else:
            self.min_values.append(min(val, self.get_min()))
        self.stack.append(val)

    def pop(self):
        self.stack.pop()
        self.min_values.pop()

    def get_size(self):
        return len(self.stack)

    def get_min(self):
        return self.min_values[len(self.min_values) - 1]

    def peek(self):
        return self.stack[len(self.stack)-1]

    def print_stack_and_min_stack(self):
        print(self.stack)
        print(self.min_values)

min_stack = Stack()
min_stack.push(5)
min_stack.push(3)
min_stack.push(10)
min_stack.push(5)
min_stack.push(0)
min_stack.print_stack_and_min_stack()
print(min_stack.get_min())
min_stack.pop()
print(min_stack.get_min())