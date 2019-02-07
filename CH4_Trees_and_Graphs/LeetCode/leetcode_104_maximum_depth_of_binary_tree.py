from CH4_Trees_and_Graphs.TreeNode import TreeNode
from collections import deque

head = TreeNode(10)
head.left = TreeNode(5)
head.right = TreeNode(15)

head.left.left = TreeNode(3)
head.left.right = TreeNode(8)
head.right.left = TreeNode(13)
head.right.right = TreeNode(18)

def bfs_get_max_depth(head):

    depth = 0
    if not head:
        return depth

    queue = deque()
    queue.append(head)

    while queue:
        size = len(queue)

        for i in range(size):
            temp = queue.pop()

            if temp.left:
                queue.appendleft(temp.left)
            if temp.right:
                queue.appendleft(temp.right)
        depth += 1

    return depth

def dfs_get_max_depth(head):
    current_level = 0
    depth = 0

    print(dfs_helper(head,depth, current_level))

def dfs_helper(head, depth, current_level):

    if not head:
        return depth

    current_level += 1
    depth = max(depth, current_level)

    if head.left:
        depth = dfs_helper(head.left, depth, current_level)

    if head.right:
        depth = dfs_helper(head.right, depth, current_level)

    current_level -= 1

    return depth

dfs_get_max_depth(head)
