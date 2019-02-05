from CH3_Stacks_and_Queues.Stack import Stack
from CH3_Stacks_and_Queues.Queue import Queue

# stack = Stack()
#
# print(stack.pop())
# stack.push(5)
# print(stack.peek())
# stack.push(56)
# stack.push(34)
# stack.push(23)
# stack.push(65)
# print(stack.peek())
# print(stack.pop())
# print(stack.peek())
#
# stack.printStack()

queue = Queue(10)

queue.en_queue(1)
queue.en_queue(1)
queue.en_queue(1)
queue.en_queue(1)
queue.en_queue(1)
queue.en_queue(1)
queue.en_queue(1)

queue.print_queue()
queue.get_size()

queue.en_queue(34)
queue.en_queue(34)
queue.en_queue(34)

queue.print_queue()
queue.get_size()

queue.de_queue()
queue.print_queue()

queue.get_size()