class Queue_using_stacks(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.flag_to_continue_popping = False

    def optimized_de_queue(self):
        if self.flag_to_continue_popping:
            print("Dequeued from 2nd stack O(1)")
            return self.stack2.pop()

        while len(self.stack1) != 1:
            self.stack2.append(self.stack1.pop())

        temp = self.stack1.pop()
        self.flag_to_continue_popping = True
        return temp

    def optimized_en_queue(self, val):
        self.flag_to_continue_popping = False
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(val)

    def print_queue(self):
        print("first stack: ",self.stack1)
        print("second stack: ",self.stack2)

queue_using_stacks = Queue_using_stacks()
queue_using_stacks.optimized_en_queue(5)
queue_using_stacks.optimized_en_queue(8)
queue_using_stacks.optimized_en_queue(3)
queue_using_stacks.optimized_en_queue(45)

queue_using_stacks.print_queue()
queue_using_stacks.optimized_de_queue()
queue_using_stacks.print_queue()
queue_using_stacks.optimized_de_queue()
queue_using_stacks.optimized_en_queue(89)
queue_using_stacks.optimized_de_queue()
queue_using_stacks.print_queue()

