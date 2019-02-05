class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return "stack is already empty"

    def peek(self):
        if not self.isEmpty():
           return self.stack[len(self.stack)-1]
        return "stack is empty"

    def printStack(self):
        print(self.stack)