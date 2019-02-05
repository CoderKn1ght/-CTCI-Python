from CH3_Stacks_and_Queues.Stack import Stack

stack = Stack()

print(stack.pop())
stack.push(5)
print(stack.peek())
stack.push(56)
stack.push(34)
stack.push(23)
stack.push(65)
print(stack.peek())
print(stack.pop())
print(stack.peek())

stack.printStack()