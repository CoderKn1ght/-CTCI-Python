from CH4_Trees_and_Graphs.TreeNode import TreeNode
from collections import deque
from sys import maxsize

root = TreeNode(3)
root.left = TreeNode(9)
# root.right = TreeNode(20)
#
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

def bfs_get_min_depth(root):

    if not root:
        return 0

    min_depth = maxsize
    current_depth = 0

    queue = deque()
    queue.append(root)

    while queue:
        size = len(queue)
        i = 0
        current_depth += 1

        for i in range(size):
            temp = queue.pop()

            if not temp.left and not temp.right:
                min_depth = min(min_depth, current_depth)

            if temp.left:
                queue.appendleft(temp.left)
            if temp.right:
                queue.appendleft(temp.right)

    return min_depth

def dfs_get_min_depth(root):
    min_depth = maxsize
    current_depth = 0

    if not root:
        return 0

    return dfs_helper(root, min_depth, current_depth)

def dfs_helper(root, min_depth, current_depth):
    current_depth += 1

    if not root.left and not root.right:
        return min(min_depth, current_depth)

    if root.left:
        min_depth = dfs_helper(root.left, min_depth, current_depth)
    if root.right:
        min_depth = dfs_helper(root.right, min_depth, current_depth)

    return min_depth

print(bfs_get_min_depth(root))