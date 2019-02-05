class Queue(object):

    def __init__(self, capacity):
        self.first = 0
        self.last = capacity - 1
        self.queue = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def ifFull(self):
        if self.size == self.capacity:
            return True
        return False

    def get_size(self):
        print(self.size)

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def en_queue(self, val):
        if self.size == self.capacity:
            return "Queue is already full"
        self.last = (self.last + 1) % self.capacity
        self.queue[self.last] = val
        self.size += 1

    def de_queue(self):
        if self.size == 0:
            return "eqeue empty"
        temp = self.queue[self.first]
        self.queue[self.first] = None
        self.first = (self.first + 1) % self.capacity
        self.size -= 1
        return temp

    def print_queue(self):
        print(self.queue)