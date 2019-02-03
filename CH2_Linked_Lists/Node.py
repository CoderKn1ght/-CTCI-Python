class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def iterate_and_print(self):
        while self:
            print(self.val)
            self = self.next

