class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def iterate_and_print(self):
        i = 0
        while self:
            print("{}: {}".format(i, self.val))
            self = self.next
            i += 1

