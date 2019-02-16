from CH4_Trees_and_Graphs.TreeNode import TreeNode
from collections import deque

head = TreeNode(6)
head.left = TreeNode(2)
head.right = TreeNode(10)

head.left.left = TreeNode(0)
head.left.right = TreeNode(4)

head.right.left = TreeNode(8)
head.right.right = TreeNode(12)

def in_order(head):

    if head == None:
        return

    in_order(head.left)
    print(head.val)
    in_order(head.right)

def in_order_using_iteration(head):
    if head == None:
        return

    stack = []
    stack.append(head)

    while stack:
        temp = stack[len(stack)-1]

        if temp.left != None:
            stack.append(temp.left)

        if temp.right != None:
            stack.append(temp.right)



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

