from CH3_Stacks_and_Queues.Stack import Stack
from sys import maxsize

min_stack = Stack()


class MinStack(object):
    def __init__(self, val):
        self.val = val
        self.min = maxsize


def push_to_stack_with_min(val):
    to_be_pushed = MinStack(val)

    if min_stack.size() == 0:
        to_be_pushed.min = val
    else:
        compare_previous_min = min_stack.peek()
        to_be_pushed.min = min(val, compare_previous_min.min)
    min_stack.push(to_be_pushed)

def peek_into_min_Stack():
    temp = min_stack.peek()
    print("{0}: {1}".format(temp.val, temp.min))


push_to_stack_with_min(6)
peek_into_min_Stack()
push_to_stack_with_min(8)
peek_into_min_Stack()
push_to_stack_with_min(4)
peek_into_min_Stack()
min_stack.pop()
peek_into_min_Stack()


