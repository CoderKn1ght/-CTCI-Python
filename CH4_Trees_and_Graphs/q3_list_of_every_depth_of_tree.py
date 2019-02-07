from CH4_Trees_and_Graphs.TreeNode import TreeNode
from collections import deque

head = TreeNode(10)
head.left = TreeNode(5)
head.right = TreeNode(15)

head.left.left = TreeNode(3)
head.left.right = TreeNode(8)
head.right.left = TreeNode(13)
head.right.right = TreeNode(18)

def using_bfs_lists_at_every_depth(head):

    if not head:
        return

    answer_list = []
    queue = deque()
    queue.append(head)

    while queue:
        size = len(queue)

        temp_list = []

        for i in range(size):
            temp_node = queue.pop()
            temp_list.append(temp_node.val)

            if temp_node.left:
                queue.appendleft(temp_node.left)

            if temp_node.right:
                queue.appendleft(temp_node.right)

        answer_list.append(temp_list)

    return answer_list

def using_dfs_lists_at_every_depth(head, list_with_tree_level_as_index, depth):

    if not head:
        return

    if len(list_with_tree_level_as_index) == depth:
        list_with_tree_level_as_index.append([head.val])
    else:
        list_with_tree_level_as_index[depth].append(head.val)

    depth += 1

    if head.left:
        using_dfs_lists_at_every_depth(head.left, list_with_tree_level_as_index, depth)

    if head.right:
        using_dfs_lists_at_every_depth(head.right, list_with_tree_level_as_index, depth)

    depth -= 1

    return list_with_tree_level_as_index

print(using_bfs_lists_at_every_depth(head))

list_with_tree_level_as_index = []
depth = 0
print(using_dfs_lists_at_every_depth(head, list_with_tree_level_as_index, depth))