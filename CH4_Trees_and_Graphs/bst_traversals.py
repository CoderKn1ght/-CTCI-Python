from CH4_Trees_and_Graphs.Node import Node
from collections import deque

head = Node(6)
head.left = Node(2)
head.right = Node(10)

head.left.left = Node(0)
head.left.right = Node(4)

head.right.left = Node(8)
head.right.right = Node(12)

def in_order(head):

    if head == None:
        return

    in_order(head.left)
    print(head.val)
    in_order(head.right)

def pre_order(head):

    if head == None:
        return

    print(head.val)
    pre_order(head.left)
    pre_order(head.right)

def post_order(head):

    if head == None:
        return

    post_order(head.left)
    post_order(head.right)
    print(head.val)

def breadth_first_search(head):

    if not head:
        return

    queue = deque()
    queue.append(head)

    while queue:
        temp = queue.pop()
        print(temp.val)

        if temp.left:
            queue.appendleft(temp.left)

        if temp.right:
            queue.appendleft(temp.right)

breadth_first_search(head)

